from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from google_auth_oauthlib.flow import Flow
import pickle

router = APIRouter()

CLIENT_SECRETS_FILE = "credentials.json"
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.modify",
    "https://www.googleapis.com/auth/gmail.send"
]
REDIRECT_URI = "http://127.0.0.1:8000/auth/callback"


@router.get("/auth/login")
def login():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI
    )
    auth_url, state = flow.authorization_url(
        access_type="offline",
        include_granted_scopes="true"
    )
    return RedirectResponse(auth_url)


@router.get("/auth/callback")
def callback(request: Request):
    state = request.query_params.get("state")
    code = request.query_params.get("code")
    if not code:
        return {"error": "Missing code parameter. Did you go through /auth/login?"}

    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI,
        state=state
    )
    flow.fetch_token(code=code)
    credentials = flow.credentials
    with open("token.pkl", "wb") as f:
        pickle.dump(credentials, f)

    return {"message": "✅ OAuth successful. Token saved to token.pkl.", "has_refresh_token": bool(credentials.refresh_token)}


@router.get("/auth/test")
def test():
    return {"ok": True, "emailAddress": "habahealth@gmail.com"}
