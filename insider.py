import requests


def get_insider_buys():

    url = "https://www.nasdaqomxnordic.com/"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    try:
        r = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        print("INSIDER TEST STATUS:", r.status_code)
        print(r.text[:300])

        return []

    except Exception as e:
        print("INSIDER ERROR:", e)
        return []