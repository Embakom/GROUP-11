from fastapi import FastAPI
from auth import router as auth_router
from email_scanner import scan_emails

app = FastAPI()
app.include_router(auth_router)


@app.get("/")
def home():
    return {"message": "Welcome to Smart Mail 🚀"}


@app.get("/scan")
def scan():
    result = scan_emails()
    return {"message": "Email scan complete.", "emails": result}
