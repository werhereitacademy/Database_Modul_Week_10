from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
import io
from backend.auth import authenticate


def download_file(file_id):
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)

    # Get file metadata
    file_metadata = service.files().get(fileId=file_id).execute()
    mime_type = file_metadata.get("mimeType")
    name = file_metadata.get("name")

    # Check if the file is a Google Docs Editors file
    if mime_type in [
        "application/vnd.google-apps.document",
        "application/vnd.google-apps.spreadsheet",
        "application/vnd.google-apps.presentation",
    ]:
        request = service.files().export_media(
            fileId=file_id,
            mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )
    else:
        request = service.files().get_media(fileId=file_id)

    file = io.BytesIO()
    downloader = MediaIoBaseDownload(file, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

    # Save the file to the disk
    with open(f"{name}", "wb") as f:
        f.write(file.getvalue())
