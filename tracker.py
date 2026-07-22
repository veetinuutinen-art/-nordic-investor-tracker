import requests
from bs4 import BeautifulSoup

URL = "https://www.inderes.fi/en/insider-transactions"

def fetch_transactions():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(URL, headers=headers, timeout=30)
    r.raise_for_status()

    with open("page.html", "w", encoding="utf-8") as f:
        f.write(r.text)

    soup = BeautifulSoup(r.text, "lxml")

    print("Title:", soup.title.text if soup.title else "No title")

    tables = soup.find_all("table")
    print("Tables:", len(tables))

    return len(tables)