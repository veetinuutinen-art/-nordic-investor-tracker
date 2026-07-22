import requests


def get_insider_buys():

    url = "https://www.nasdaqomxnordic.com/api/insidertrading"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "application/json"
    }

    try:
        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print(r.text[:500])

        if r.status_code != 200:
            return []

        data = r.json()

        results = []

        for item in data[:5]:
            results.append(
                f"🦅 {item}"
            )

        return results

    except Exception:
        return []