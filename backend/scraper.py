import requests
from bs4 import BeautifulSoup

def scrape_wikipedia(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
    }

    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    title = soup.find("h1").text

    paragraphs = soup.find_all("p")
    content = ""

    for p in paragraphs:
        content += p.text

    return {
        "title": title,
        "content": content[:5000]
    }

