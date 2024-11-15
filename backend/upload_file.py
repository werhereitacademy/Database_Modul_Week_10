from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from backend.auth import authenticate


def update_file(
    file_id,
    filename,
    mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
):

    authenticate()  # guncelleme icin

    # kimlik dogrulama
    creds = Credentials.from_authorized_user_file(
        "token.json", ["https://www.googleapis.com/auth/drive"]
    )

    # Google Drive API servisi baslatma
    service = build("drive", "v3", credentials=creds)

    try:
        # MediaFileupload;hangi dosyanin yuklenecegini belirtir. Google'dan gelen hazir bir sinif...
        # Mimetype; dosyanin turu...Resumable; yuklemenin kesilip devam edebilmesi icin.
        media = MediaFileUpload(filename, mimetype=mimeType, resumable=True)

        # dosya guncelleme
        updated_file = (
            service.files().update(fileId=file_id, media_body=media).execute()
        )

        # Güncellenen dosyanın adı
        return updated_file.get("name")

    except Exception as e:
        print(f"Dosya güncellenirken hata oluştu: {e}")
        return None
