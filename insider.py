import requests
from bs4 import BeautifulSoup
from datetime import datetime


COMPANIES = {
    "Nokia": "https://www.nokia.com/about-us/investors/",
    "Sampo": "https://www.sampo.com/investors/",
    "Kone": "https://www.kone.com/en/investors/",
    "Neste": "https://www.neste.com/investors",
    "Fortum": "https://www.fortum.com/investors"
}


def get_insider_buys():

    alerts = []

    keywords = [
        "manager transaction",
        "insider",
        "purchase",
        "buy",
        "acquisition"
    ]

    for company, url in COMPANIES.items():

        try:
            r = requests.get(
                url,
                headers={
                    "User-Agent": "Mozilla/5.0"
                },
                timeout=20
            )

            text = r.text.lower()

            found = False

            for word in keywords:
                if word in text:
                    found = True

            if found:
                alerts.append(
                    f"🦅 {company}\n"
                    f"Mahdollinen sisäpiiri-ilmoitus löytyi\n"
                    f"{datetime.now().strftime('%d.%m.%Y')}"
                )

        except Exception:
            continue


    return alerts