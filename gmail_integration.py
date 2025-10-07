from googleapiclient.discovery import build
import pickle


def get_service():
    with open("token.pkl", "rb") as f:
        creds = pickle.load(f)
    service = build("gmail", "v1", credentials=creds)
    return service


def list_messages(service, query=""):
    results = service.users().messages().list(userId="me", q=query).execute()
    messages = results.get("messages", [])
    return messages


def get_message(service, msg_id):
    msg = service.users().messages().get(
        userId="me", id=msg_id, format="full").execute()
    return msg


def move_to_trash(service, msg_id):
    service.users().messages().trash(userId="me", id=msg_id).execute()
