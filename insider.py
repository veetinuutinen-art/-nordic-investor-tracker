import requests
from bs4 import BeautifulSoup


def get_insider_buys():

    url = "https://www.nasdaqomxnordic.com/insidertransactions"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    soup = BeautifulSoup(r.text, "html.parser")

    buys = []

    for row in soup.find_all("tr"):
        text = row.get_text(" ", strip=True)

        if "Buy" in text or "Purchase" in text:
            buys.append(text)

    return buys[:5]