from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import requests

app = FastAPI()

# Allow Netlify frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

quiz_history = []

@app.get("/")
def root():
    return {"message": "AI Wiki Quiz Generator API is running"}

@app.get("/generate-quiz")
def generate_quiz(url: str):
    title = url.split("/")[-1].replace("_", " ")

    quiz = [
        {
            "question": f"Who is {title}?",
            "options": ["Scientist", "Actor", "Politician", "Writer"],
            "answer": "Scientist",
            "explanation": f"{title} is best known as a scientist."
        },
        {
            "question": f"What is {title} famous for?",
            "options": [
                "Computer Science",
                "Sports",
                "Music",
                "Movies"
            ],
            "answer": "Computer Science",
            "explanation": f"{title} made major contributions to computer science."
        }
    ]

    data = {
        "title": title,
        "url": url,
        "quiz": quiz
    }

    quiz_history.append(data)
    return data

@app.get("/history")
def history():
    return quiz_history
