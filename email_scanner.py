import pickle
from googleapiclient.discovery import build


def scan_emails():
    # Load credentials
    with open("token.pkl", "rb") as f:
        credentials = pickle.load(f)

    service = build("gmail", "v1", credentials=credentials)

    # Retrieve messages
    results = service.users().messages().list(userId="me", maxResults=10).execute()
    messages = results.get("messages", [])

    email_data = []
    for msg in messages:
        msg_detail = service.users().messages().get(
            userId="me", id=msg["id"]).execute()
        snippet = msg_detail.get("snippet", "")
        email_data.append({"id": msg["id"], "snippet": snippet})

    return email_data
