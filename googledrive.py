from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
from google.oauth2 import service_account
#from google calendar integration
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

import pandas as pd
import io, os, datetime

class GoogleDriveFileManager:
    fileid_dict = {
        "Basvurular": "11ys9OsUiqBjZR676nLgXKpPrg7ykkfZ2",
        "Mulakatlar": "1jBBNrMt-GUAaPot7cGidEdC1dCZ2RYHK",
        "Mentor": "1uz9Dn1N3tWK1y83JQG3E-PJ9sLwkLUy_",
        "Kullanicilar": "1pPzybfDOgN_CnP7nfaDc2L2gHgeBkKqJ"
    }
    def __init__(self, file, servicefile="seracc.json"):
        try:
            self.scopes = ["https://www.googleapis.com/auth/drive"]
            self.service = servicefile
            if file not in GoogleDriveFileManager.fileid_dict.keys():
                self.file = file
            else:
                self.file = GoogleDriveFileManager.fileid_dict[file]
            self.creds = service_account.Credentials.from_service_account_file(self.service, scopes=self.scopes)
            self.drive_service = build("drive", "v3", credentials=self.creds)
            self.excel_file = None
        except Exception as e:
            print(f"An error occurred: {e}")

    def getExcelFile(self):
        try:
            file_metadata = self.drive_service.files().get(fileId=self.file).execute()
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
        try:
            request = self.drive_service.files().get_media(fileId=self.file)
            file_stream = io.BytesIO()
            downloader = MediaIoBaseDownload(file_stream, request)
            done = False
            while done is False:
                status, done = downloader.next_chunk()
            file_stream.seek(0)
            self.excel_file = pd.read_excel(file_stream, engine="openpyxl")
            return self.excel_file
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None
        
    def search_data(self, column_name, search_value, case_sensitive = False):
        try:
            matching_rows = self.excel_file[self.excel_file[column_name].str.lower() == search_value.lower()]
            return matching_rows
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def mask_data(self, column_name, search_value):
        try:
            mask_value = self.excel_file[column_name].str.contains(search_value, na=False)
            matching_rows = self.excel_file[mask_value]
            return matching_rows
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    def search_data_different(self, column_name, search_value):
        try:
            matching_rows = self.excel_file[self.excel_file[column_name].str.lower() != search_value.lower()]
            return matching_rows
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
    
    def search_data_multiple(self, serach_dict):
        try:
            query_string = " & ".join([f"(df['{col}'] == '{val}')" for col, val in serach_dict.items()])
            matching_rows = self.excel_file[eval(query_string)]
            return matching_rows
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def full_text_search(self, search_value):
        try:
            # matching_rows = self.excel_file[self.excel_file.applymap(lambda x: search_value.lower() in str(x).lower()).any(axis=1)]
            matching_rows = self.excel_file[self.excel_file.apply(lambda row: any(search_value.lower() in str(cell).lower() for cell in row), axis=1)]
            return matching_rows
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    def update_row(self, row_index, column_name, new_value):
        try:
            self.excel_file.at[row_index, column_name] = new_value
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def save_excel_file(self):
        try:
            self.excel_file.to_excel("temp.xlsx", index=False)
            media = MediaFileUpload("temp.xlsx", mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")

            self.drive_service.files().update(
                fileId=self.file,
                media_body=media
            ).execute()
            return True
        except Exception as e:
            print(f"An error occurred: {e}")
            return False
"""----------------------------------------------------------------------------------------"""
# Google Calendar Integration
class GoogleCalendarManager:
    def __init__(self, service_account_file):
        try:
            self.service_account_file = service_account_file
            self.scopes = ["https://www.googleapis.com/auth/calendar.readonly"]

            self.credentials = self.get_credentials()
            print("Credentials obtained successfully.")
        except HttpError as error:
            print('An error occurred: %s' % error)
    
    def get_credentials(self):
        creds = None
        
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', self.scopes)

        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    "seracc_calendar.json", self.scopes
                )
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(creds.to_json())
        return creds

    def get_calendar_events(self, calendar_id="primary"):
        try:
            service = build("calendar", "v3", credentials=self.credentials)

            now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time

            events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                                maxResults=50, singleEvents=True,
                                                orderBy='startTime').execute()
            self.events = events_result.get('items', [])
            print("Events retrieved successfully.")
        except HttpError as error:
            print(f"An error occurred: {error}")
"""----------------------------------------------------------------------------------------"""
def google_drive_test():
    #GoogleDriveFileManager
    Obj_Excel_File = GoogleDriveFileManager("Mentor")
    Obj_Excel_File.getExcelFile()

    # arama_sonucu = Obj_Excel_File.excel_file[(Obj_Excel_File.excel_file["kullanici"] == "musta") & (Obj_Excel_File.excel_file["parola"] == "12345")]
    print(Obj_Excel_File.excel_file)
    #print(f"ID: {arama_sonucu.index[0]}, Kullanıcı Adı: {arama_sonucu['kullanici'].values[0]}, Parola: {arama_sonucu['parola'].values[0]}")
    # if Obj_Excel_File.update_row(6,"parola","q"):
    #     Obj_Excel_File.save_excel_file()
    # else:
    #     print("Update failed!!!")    

def google_calendar_test():
    Obj_Calendar = GoogleCalendarManager("seracc_calendar.json")
    Obj_Calendar.get_calendar_events()
    print(Obj_Calendar.events)
    if not Obj_Calendar.events:
        print('No upcoming events found.')
    else:
        if Obj_Calendar.events:
            for event in Obj_Calendar.events:
                start = event['start'].get('dateTime', event['start'].get('date'))
                participant = []
                organizer = event['organizer']['email']
                if "attendees" in event:
                    for attendee in event['attendees']:
                        if organizer != attendee["email"] and attendee["email"] not in participant:
                            participant.append(attendee["email"])
                action_name = event["summary"]
                print(f"{action_name} - {start} - {organizer}",end="") 
                for i in range(len(participant)):
                    print(f" - {participant[i]}",end="")
                print()
"""
[{'kind': 'calendar#event', 'etag': '"3478761919592000"', 'id': '0degirqb84928efvg6nb19gl65_20250218T213000Z', 'status': 'confirmed', 
  'htmlLink': 'https://www.google.com/calendar/event?eid=MGRlZ2lycWI4NDkyOGVmdmc2bmIxOWdsNjVfMjAyNTAyMThUMjEzMDAwWiBtdXN0YWZhLm1ndW5kb2dkdUBt', 'created': '2025-01-28T21:20:15.000Z', 
  'updated': '2025-02-12T17:22:39.796Z', 'summary': 'VIT Group Meeting', 'creator': {'email': 'mustafa.mgundogdu@gmail.com', 'self': True}, 
  'organizer': {'email': 'mustafa.mgundogdu@gmail.com', 'self': True}, 'start': {'dateTime': '2025-02-18T22:30:00+01:00', 'timeZone': 'Europe/Amsterdam'}, 
  'end': {'dateTime': '2025-02-18T23:30:00+01:00', 'timeZone': 'Europe/Amsterdam'}, 'recurringEventId': '0degirqb84928efvg6nb19gl65_R20250218T213000', 
  'originalStartTime': {'dateTime': '2025-02-18T22:30:00+01:00', 'timeZone': 'Europe/Amsterdam'}, 'iCalUID': '0degirqb84928efvg6nb19gl65_R20250218T213000@google.com', 
  'sequence': 0, 'attendees': [{'email': 'mustafa.mgundogdu@gmail.com', 'organizer': True, 'self': True, 'responseStatus': 'accepted'}, 
  {'email': 'nesli.utuk@gmail.com', 'responseStatus': 'needsAction'}, {'email': 'yasinsinan1@gmail.com', 'responseStatus': 'accepted'}, 
  {'email': 'kahramandal@gmail.com', 'responseStatus': 'needsAction'}], 'hangoutLink': 'https://meet.google.com/hvt-iprs-rsv', 
  'conferenceData': {'entryPoints': [{'entryPointType': 'video', 'uri': 'https://meet.google.com/hvt-iprs-rsv', 'label': 'meet.google.com/hvt-iprs-rsv'}], 
  'conferenceSolution': {'key': {'type': 'hangoutsMeet'}, 'name': 'Google Meet', 'iconUri': 'https://fonts.gstatic.com/s/i/productlogos/meet_2020q4/v6/web-512dp/logo_meet_2020q4_color_2x_web_512dp.png'}, 
  'conferenceId': 'hvt-iprs-rsv'}, 'reminders': {'useDefault': True}, 'eventType': 'default'}]
"""
if __name__ == "__main__":
    # google_drive_test()
    pass
    # GoogleCalendarManager
    google_calendar_test()