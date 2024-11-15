from backend.auth import authenticate
from googleapiclient.discovery import build


def list_drive_files():
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)

    results = (
        service.files()
        .list(
            pageSize=10,
            fields="nextPageToken, files(id, name)",
        )
        .execute()
    )
    items = results.get("files", [])

    if not items:
        return []
    else:
        return items
