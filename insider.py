import requests
from datetime import datetime
from bs4 import BeautifulSoup

from insider_database import (
    init_insider_db,
    already_seen,
    save_seen
)


COMPANIES = {
    "Nokia": "https://www.nokia.com/about-us/investors/",
    "Sampo": "https://www.sampo.com/investors/",
    "Kone": "https://www.kone.com/en/investors/",
    "Neste": "https://www.neste.com/investors",
    "Fortum": "https://www.fortum.com/investors"
}


def get_insider_buys():

    init_insider_db()

    alerts = []

    keywords = [
        "manager transaction",
        "insider",
        "purchase",
        "buy"
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

            soup = BeautifulSoup(
                r.text,
                "html.parser"
            )

            text = soup.get_text(
                " ",
                strip=True
            ).lower()


            for word in keywords:

                if word in text:

                    message = (
                        f"{company} "
                        f"{word} "
                        f"{datetime.now().strftime('%d.%m.%Y')}"
                    )

                    if already_seen(company, message):
                        break

                    save_seen(company, message)

                    alerts.append(
                        f"🦅 {company}\n"
                        f"Mahdollinen sisäpiiri-ilmoitus\n"
                        f"Avainsana: {word}"
                    )

                    break


        except Exception:
            continue


    return alerts