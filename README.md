# Smart Mail Project

Smart Mail is a Python-based FastAPI application that allows you to securely connect to Gmail, scan emails, and manage them programmatically. The project integrates Google OAuth for authentication and supports reading, modifying, and sending emails.

---

## Features

* OAuth 2.0 login with Google
* Save and refresh tokens automatically (`token.pkl`)
* Scan and list emails from Gmail
* Retrieve email snippets for easy viewing
* Ready-to-use FastAPI endpoints

---

## Project Structure

```
Smart-Mail/
│
├─ main.py             # Entry point for FastAPI server
├─ auth.py             # OAuth login and callback handlers
├─ email_scanner.py    # Gmail email scanning functionality
├─ credentials.json    # Google OAuth client secrets (add your own)
├─ token.pkl           # Saved OAuth token (auto-generated)
├─ requirements.txt    # Required Python packages
└─ README.md           # Project documentation
```

---

## Setup Instructions

1. **Clone the repository:**

```bash
git clone <your-repo-url>
cd Smart-Mail
```

2. **Create a virtual environment (optional but recommended):**

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Add Google OAuth credentials:**

* Download your `credentials.json` from Google Cloud Console.
* Place it in the project root.

5. **Run the server:**

```bash
uvicorn main:app --reload
```

6. **Open in browser:**

* Home: `http://127.0.0.1:8000/`
* Login: `http://127.0.0.1:8000/auth/login`
* Scan Emails: `http://127.0.0.1:8000/scan`

---

## API Endpoints

| Endpoint         | Method | Description                                    |
| ---------------- | ------ | ---------------------------------------------- |
| `/`              | GET    | Returns a welcome message                      |
| `/auth/login`    | GET    | Initiates Google OAuth login                   |
| `/auth/callback` | GET    | Callback URL for OAuth                         |
| `/scan`          | GET    | Scans Gmail inbox and returns latest 10 emails |

---

## Notes

* **Token Handling:** The `token.pkl` file is generated after successful OAuth login and contains your access and refresh tokens.
* **Privacy:** Never commit `credentials.json` with real credentials to a public repository.
* **Email Scan:** Currently fetches the latest 10 emails and their snippets.

---

## Contributing

1. Fork the repo
2. Create a new branch: `git checkout -b feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature-name`
5. Open a Pull Request

---

## License

This project is open-source and available under the MIT License.

---

## Screenshots

![Home Page]
![Scan Result]

---

**Smart Mail** – Make Gmail management smarter and easier!
