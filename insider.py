import requests
from bs4 import BeautifulSoup
from datetime import datetime

from insider_database import (
    init_insider_db,
    already_seen,
    save_seen
)


COMPANIES = {
    "Nokia": "https://www.nokia.com/about-us/news/releases/",
    "Sampo": "https://www.sampo.com/media/releases/",
    "Kone": "https://www.kone.com/en/news-and-releases/",
    "Neste": "https://www.neste.com/news",
    "Fortum": "https://www.fortum.com/media",

    "Volvo": "https://www.volvogroup.com/en/news-and-media/news.html",
    "Investor AB": "https://www.investorab.com/media/news/",
    "Saab": "https://www.saab.com/news",

    "Novo Nordisk": "https://www.novonordisk.com/news-and-media/news-and-ir-materials.html",
    "Equinor": "https://www.equinor.com/news"
}


KEYWORDS = [
    "insider transaction",
    "manager transaction",
    "person discharging managerial responsibilities",
    "pdmr",
    "board member purchase",
    "ceo purchase",
    "director purchase"
]


def get_insider_buys():

    init_insider_db()

    alerts = []

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

            headlines = []

            for h in soup.find_all(
                ["h1", "h2", "h3", "a"]
            ):
                text = h.get_text(
                    " ",
                    strip=True
                )

                if text:
                    headlines.append(text)


            for headline in headlines[:50]:

                low = headline.lower()

                # Poistetaan yhtiöiden omat takaisinostot
                if (
                    "buy-back" in low
                    or "buyback" in low
                    or "share buy-back" in low
                ):
                    continue


                for word in KEYWORDS:

                    if word in low:

                        alert_id = (
                            f"{company}-{headline}"
                        )

                        if already_seen(
                            company,
                            alert_id
                        ):
                            continue


                        save_seen(
                            company,
                            alert_id
                        )


                        alerts.append(
                            "🦅 SISÄPIIRIKAUPPA\n\n"
                            f"Yhtiö: {company}\n"
                            f"Otsikko: {headline}\n"
                            f"Päivä: "
                            f"{datetime.now().strftime('%d.%m.%Y')}"
                        )

                        break


        except Exception:
            continue


    return alerts