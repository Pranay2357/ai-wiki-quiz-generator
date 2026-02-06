from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from scraper import scrape_wikipedia
from quiz_generator import generate_quiz
from storage import save_quiz, get_all_quizzes

app = FastAPI(title="AI Wiki Quiz Generator")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ ROOT ENDPOINT
@app.get("/")
def root():
    return {"message": "AI Wiki Quiz Generator API is running"}

# ✅ GENERATE QUIZ
@app.get("/generate-quiz")
def generate_quiz_api(url: str):
    if not url:
        return {"error": "URL is required"}

    data = scrape_wikipedia(url)
    quiz = generate_quiz(data["content"])

    result = {
        "url": url,
        "title": data["title"],
        "quiz": quiz
    }

    save_quiz(result)
    return result

# ✅ HISTORY
@app.get("/history")
def quiz_history():
    return get_all_quizzes()

