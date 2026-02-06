from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend (Netlify) to call backend (Render)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# ROOT CHECK
# ---------------------------
@app.get("/")
def root():
    return {"message": "AI Wiki Quiz Backend is running"}

# ---------------------------
# GENERATE QUIZ (GET)
# ---------------------------
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

# ---------------------------
# HISTORY (GET)
# ---------------------------
@app.get("/history")
def history():
    return []
