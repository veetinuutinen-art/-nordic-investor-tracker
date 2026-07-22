import requests
from datetime import datetime


def get_insider_buys():

    url = "https://www.avanza.se/_api/insider-transactions"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        if r.status_code != 200:
            return []

        data = r.json()

        results = []

        for item in data[:5]:
            results.append(
                f"{item}"
            )

        return results

    except Exception:
        return []