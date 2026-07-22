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
    "Fortum": "https://www.fortum.com/investors",

    "Volvo": "https://www.volvogroup.com/en/investors.html",
    "Investor AB": "https://www.investorab.com/investors/",
    "Saab": "https://www.saab.com/investors",

    "Novo Nordisk": "https://www.novonordisk.com/investors.html",
    "A.P. Moller - Maersk": "https://investor.maersk.com/",

    "Equinor": "https://www.equinor.com/investors",
    "DNB": "https://www.ir.dnb.no/"
}


def get_insider_buys():

    init_insider_db()

    alerts = []

    keywords = [
        "manager transaction",
        "insider transaction",
        "insider purchase",
        "share purchase",
        "purchased shares"
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
            )

            lower = text.lower()


            found_word = None

            for word in keywords:
                if word in lower:
                    found_word = word
                    break


            if found_word:

                message = (
                    f"{company}-{found_word}-"
                    f"{datetime.now().strftime('%d.%m.%Y')}"
                )


                if already_seen(company, message):
                    continue


                save_seen(
                    company,
                    message
                )


                alerts.append(
                    "🦅 SISÄPIIRI\n\n"
                    f"Yhtiö: {company}\n"
                    f"Havainto: {found_word}\n"
                    f"Päivä: "
                    f"{datetime.now().strftime('%d.%m.%Y')}"
                )


        except Exception:
            continue


    return alerts