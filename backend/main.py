from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROOT TEST
@app.get("/")
def root():
    return {"message": "AI Wiki Quiz Backend is running"}

# GENERATE QUIZ (GET)
@app.get("/generate-quiz")
def generate_quiz(url: str):
    return {
        "title": "Alan Turing",
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

# HISTORY
@app.get("/history")
def history():
    return []
