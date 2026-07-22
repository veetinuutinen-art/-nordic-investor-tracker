import os
import json
import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

URL = "https://www.inderes.fi/en/insider-transactions"

def send_message(text):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": text
        },
        timeout=30
    )

try:
    r = requests.get(URL, timeout=30)

    if r.status_code == 200:
        send_message(
            "✅ Nordic Investor Tracker toimii!\n\n"
            f"Inderes vastasi onnistuneesti ({r.status_code}).\n"
            "Seuraavaksi lisätään varsinainen sisäpiiritapahtumien haku."
        )
    else:
        send_message(
            f"⚠️ Inderes vastasi koodilla {r.status_code}"
        )

except Exception as e:
    send_message(f"❌ Virhe:\n{e}")