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





**👤 Author**
Nagasri Maturi






