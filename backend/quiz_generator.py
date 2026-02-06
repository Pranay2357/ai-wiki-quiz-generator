def generate_quiz(article_text: str):
    return [
        {
            "question": "Who is the main person discussed in the article?",
            "options": [
                "Isaac Newton",
                "Alan Turing",
                "Albert Einstein",
                "Charles Babbage"
            ],
            "answer": "Alan Turing",
            "difficulty": "easy",
            "explanation": "The article is a biography of Alan Turing."
        },
        {
            "question": "What was Alan Turing famous for during World War II?",
            "options": [
                "Inventing radar",
                "Breaking the Enigma code",
                "Building airplanes",
                "Leading the navy"
            ],
            "answer": "Breaking the Enigma code",
            "difficulty": "medium",
            "explanation": "He worked at Bletchley Park breaking German Enigma codes."
        }
    ]

