import requests
from bs4 import BeautifulSoup

URL = "https://www.inderes.fi/en/insider-transactions"

def fetch_transactions():
    response = requests.get(
        URL,
        headers={
            "User-Agent": "Mozilla/5.0"
        },
        timeout=30,
    )

    response.raise_for_status()

    soup = BeautifulSoup(response.text, "lxml")

    print("Sivu haettu onnistuneesti.")
    print("Sivun koko:", len(response.text))

    return response.text