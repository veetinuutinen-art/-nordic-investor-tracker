import requests
from bs4 import BeautifulSoup
from datetime import datetime


WATCHLIST = [
    "Nokia",
    "Sampo",
    "Kone",
    "Neste",
    "Fortum",
    "Volvo",
    "Investor",
    "Saab",
    "Novo Nordisk",
]


def fetch_transactions():

    url = "https://www.nasdaqomxnordic.com/news/insidertrading"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    r = requests.get(
        url,
        headers=headers,
        timeout=30
    )

    soup = BeautifulSoup(
        r.text,
        "html.parser"
    )

    tables = soup.find_all("table")

    return tables


def run_tracker():

    tables = fetch_transactions()

    if not tables:
        return "⚠️ Ei löytynyt taulukoita."

    now = datetime.now().strftime("%d.%m.%Y %H:%M")

    msg = (
        "📊 Nordic Investor Tracker\n\n"
        f"⏱ Päivitys: {now}\n"
        f"📄 Löytyi {len(tables)} datataulukkoa\n\n"
        "Seuranta käynnissä."
    )

    return msg