from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

def get_emails(token: str, refresh_token: str, scopes: list):
    creds = Credentials(token=token, refresh_token=refresh_token, scopes=scopes)
    service = build("gmail", "v1", credentials=creds)

    results = service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])

    email_list = []
    for msg in messages:
        msg_detail = service.users().messages().get(userId="me", id=msg["id"]).execute()
        email_list.append({
            "id": msg["id"],
            "snippet": msg_detail["snippet"]
        })
    return email_list
