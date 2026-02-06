from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Wiki Quiz Backend is running"}

@app.get("/generate-quiz")
def generate_quiz(url: str):
    return {
        "title": "Alan Turing",
        "source_url": url,
        "quiz": [
            {
                "question": "Who was Alan Turing?",
                "options": [
                    "Mathematician",
                    "Actor",
                    "Politician",
                    "Writer"
                ],
                "answer": "Mathematician",
                "explanation": "Alan Turing was a mathematician and computer scientist."
            }
        ]
    }

@app.get("/history")
def history():
    return []
