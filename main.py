
from fastapi import FastAPI
from fastapi import HTTPException
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime
from openai import OpenAI
import os


app = FastAPI()

@app.get("/")
def root():
    return {"message": "FastAPI is running"}

DATABASE_URL = "sqlite:///notes.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

Base.metadata.create_all(engine)

 
@app.get("/notes")
def get_notes(limit: int = 10, offset: int = 0, q: str = None):
    db = SessionLocal()

    query = db.query(Note)
    if q:
        query = query.filter(Note.content.contains(q))

    notes = query.offset(offset).limit(limit).all()
    db.close()

    return notes


# GET /notes → fetch notes

@app.post("/notes")
def create_note(note: dict):
    db = SessionLocal()

    new_note = Note(
        title=note["title"],
        content=note["content"]
    )

    db.add(new_note)
    db.commit()
    db.refresh(new_note)  # gets id + created_at
    db.close()

    return {
        "id": new_note.id,
        "title": new_note.title,
        "content": new_note.content,
        "created_at": new_note.created_at
    }


# OpenAI client

client = OpenAI(api_key="your_api_key")


# POST /notes/summarize

@app.post("/notes/summarize")
def summarize_note(data: dict):
    try:
        text = data["text"]

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": f"Summarize the text. Give summary, bullets, and tags:\n{text}"
                }
            ]
        )

        summary_text = response.choices[0].message.content

        return {
            "summary": summary_text,
            "bullets": summary_text.split(".")[:3],
            "tags": ["notes", "ai"]
        }

    except Exception as e:
        # This will show the REAL error instead of silent 500

        raise HTTPException(status_code=500, detail=str(e))
