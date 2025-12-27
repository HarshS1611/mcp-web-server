# ArmorIQ MCP Banking Server

A simple **Python-based MCP Server** built using **FastAPI** that simulates a basic banking system.
The server exposes REST APIs for account management and transactions, backed by a SQL database, and is designed to be easily deployable on a public cloud.

Note: This service is deployed on Render’s free tier and may experience brief cold-start delays after periods of inactivity; this does not impact functionality or security evaluation.

---

##  Features

* Account creation
* Deposit funds
* Withdraw funds
* Balance inquiry
* Transaction history
* Swagger UI documentation
* Supports **SQLite (local)** and **PostgreSQL (Neon / production)**

---

##  Tech Stack

* **Python 3.9+**
* **FastAPI**
* **SQLAlchemy**
* **SQLite** (local development)
* **PostgreSQL (Neon)** for persistent cloud storage
* **Uvicorn** (ASGI server)

---

## 📂 Project Structure

```
mcp-web-server/
├── app/
│   ├── main.py          # FastAPI entry point
│   ├── database.py      # DB configuration
│   ├── models.py        # SQLAlchemy models
│   ├── schemas.py       # Pydantic schemas
│   └── crud.py          # Business logic
│
├── .env                 # Environment variables (local only)
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup & Run Locally (SQLite)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/mcp-web-server.git
cd mcp-web-server
```

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate     # macOS / Linux
venv\Scripts\activate        # Windows
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Configure SQLite Database

In `app/database.py`:

```python
DATABASE_URL = "sqlite:////tmp/bank.db"
```

SQLite requires no extra setup.

---

### 5️⃣ Run the Server

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

You can now test all banking endpoints via Swagger UI.

---

##  Setup & Run Locally (PostgreSQL using Neon)

### 1️⃣ Create a Neon PostgreSQL Database

* Sign up at [https://neon.tech](https://neon.tech)
* Create a new project
* Copy the **connection string**

Example:

```text
postgresql://user:password@ep-xyz.us-east-1.aws.neon.tech/neondb
```

---

### 2️⃣ Create `.env` File

At project root:

```env
DATABASE_URL=postgresql://user:password@ep-xyz.neon.tech/neondb
```

⚠️ Do **not** commit `.env` to GitHub.

---

### 3️⃣ Load Environment Variables

Ensure `database.py` includes:

```python
from dotenv import load_dotenv
load_dotenv()
```

And reads:

```python
DATABASE_URL = os.getenv("DATABASE_URL")
```

---

### 4️⃣ Run Server with PostgreSQL

```bash
uvicorn app.main:app --reload
```

The database tables will be created automatically in Neon.

---

## 🌐 Deploying to Render (Public URL)

### 1️⃣ Push Code to GitHub

```bash
git add .
git commit -m "feat: configure Neon PostgreSQL for persistent data storage"
git push origin main
```

---

### 2️⃣ Create Render Web Service

1. Go to [https://render.com](https://render.com)
2. Create **New Web Service**
3. Connect your GitHub repository

---

### 3️⃣ Render Configuration

| Setting       | Value                                              |
| ------------- | -------------------------------------------------- |
| Runtime       | Python                                             |
| Build Command | `pip install -r requirements.txt`                  |
| Start Command | `uvicorn app.main:app --host 0.0.0.0 --port 10000` |

---

### 4️⃣ Add Environment Variable on Render

| Key            | Value                             |
| -------------- | --------------------------------- |
| `DATABASE_URL` | Neon PostgreSQL connection string |

Redeploy the service.

---

### 5️⃣ Access Deployed Server

After deployment, open:

```
https://<your-render-app>.onrender.com/docs
```

This is the **public MCP server URL** used for ArmorIQ security scanning.

---

## 🔐 Security Scanning (ArmorIQ Assignment)

* Scan the deployed URL using ArmorIQ tools:

  * ArmorIQ Sentry VS Code Extension
![alt text](image.png)


  * ArmorIQ public scanner on the landing page
![alt text](image-1.png)
---

## 📬 Submission Checklist

* ✅ Public Render URL
* ✅ GitHub repository link
* ✅ Sentry scan screenshots
* ✅ Landing page scan screenshots
* ✅ README with setup & deployment instructions



