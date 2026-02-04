# 📝 FastAPI Notes App (Mini Project)

A simple FastAPI backend application that allows users to create and retrieve notes stored in a SQLite database, with optional AI-powered text summarization using an external LLM API.

This project is built as a **Level-0 backend mini project** to demonstrate API development, database integration, and external API usage.

---

## 🚀 Features

- FastAPI backend
- SQLite database (auto-created)
- Create and fetch notes
- Pagination and optional search
- AI summarization integration (LLM API)
- Auto-generated API documentation (Swagger UI)

## 🗄️ Database

### Table: `notes`

| Column       | Type     | Description |
|-------------|----------|-------------|
| id          | Integer  | Primary key (auto-increment) |
| title       | String   | Title of the note |
| content     | String   | Note content |
| created_at  | DateTime | Timestamp when the note is created |

The database uses **SQLite** and is created automatically when the app runs.

---

## 📌 API Endpoints

### 1️⃣ POST `/notes`
Create and save a new note.


{
  "title": "Test note",
  "content": "FastAPI project completed"
}


**2️⃣ GET /notes**

Fetch saved notes with pagination and optional search.

Query Parameters

limit (default: 10)

offset (default: 0)

q (optional search text)

**3️⃣ POST /notes/summarize**

Summarize text using an external LLM API.

**🔑 External API Integration**

Service: OpenAI (LLM API)

Purpose: Text summarization

Integration Type: Server-side API call using API key

***⚙️ How to Run Locally***
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run the server
uvicorn main:app --port 8001

3️⃣ Open Swagger UI
http://127.0.0.1:8001/docs



**📸 Screenshots / Demo**

Screenshots are available in the screenshots/ folder:

swagger_ui.png – Swagger UI showing all endpoints

post_notes.png – Creating a new note

get_notes.png – Fetching notes from the database

These screenshots demonstrate that all core APIs are working correctly.

**⚠️ Tradeoffs and Design Decisions**
SQLite instead of PostgreSQL

Chosen for simplicity and zero setup

Not suitable for high-concurrency production systems

Dictionary-based request bodies

Easy to understand and beginner-friendly

Less strict validation than Pydantic models

External AI API dependency

Demonstrates real-world LLM integration

Execution depends on API quota and billing

No authentication

Focused on backend fundamentals

Authentication can be added in future versions

**🧠 Lessons Learned**

FastAPI provides clean APIs with automatic documentation

SQLAlchemy simplifies database interactions

Pagination and search improve API usability

External APIs introduce real-world constraints like quota and billing

Proper error handling is critical for debugging

Clean project structure improves review quality

**🚀 Future Improvements**

Add Pydantic models for request/response validation

Add authentication and authorization

Use PostgreSQL instead of SQLite

Add unit tests

Dockerize and deploy the application

**👤 Author**
Nagasri Maturi




