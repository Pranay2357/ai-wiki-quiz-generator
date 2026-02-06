import os
import json
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-pro",
    google_api_key=os.getenv("GEMINI_API_KEY"),
    temperature=0.5
)

def generate_ai_quiz(content: str):
    prompt = f"""
Generate EXACTLY 5 multiple-choice quiz questions from the content below.

Return ONLY valid JSON in this exact format:

[
  {{
    "question": "...",
    "options": ["A", "B", "C", "D"],
    "answer": "...",
    "difficulty": "easy | medium | hard",
    "explanation": "..."
  }}
]

NO markdown.
NO extra text.
ONLY JSON.

Content:
{content}
"""

    response = llm.invoke(prompt)

    try:
        text = response.content.strip()

        # safety: remove accidental code fences
        text = text.replace("```json", "").replace("```", "")

        return json.loads(text)

    except Exception as e:
        # fallback so API NEVER crashes
        return [
            {
                "question": "AI generation failed",
                "options": ["Retry", "Retry", "Retry", "Retry"],
                "answer": "Retry",
                "difficulty": "easy",
                "explanation": "Gemini returned invalid JSON"
            }
        ]

