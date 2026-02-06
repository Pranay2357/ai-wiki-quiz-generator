# AI Wiki Quiz Generator

An AI-powered web application that generates quiz questions from any Wikipedia article URL.

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript
- Hosted on Netlify

### Backend
- Python
- FastAPI
- Uvicorn
- Hosted on Render

---

## Features

- Generate quiz questions from Wikipedia articles
- Multiple-choice questions with answers & explanations
- View previously generated quizzes (history)
- Clean UI with tab-based navigation
- Fully deployed frontend and backend

---

## Live Demo

- **Frontend:** https://lively-klepon-1c02b8.netlify.app  
- **Backend API:** https://ai-wiki-quiz-backend-s908.onrender.com

---

## How to Run Locally

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
