import os
import requests
from tracker import fetch_transactions

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg,
        },
        timeout=30,
    )


try:
    html = fetch_transactions()

    send(
        "✅ Tracker toimii\n\n"
        f"Haettiin {len(html)} merkkiä Inderesiltä."
    )

except Exception as e:
    send(f"❌ Virhe:\n{e}")