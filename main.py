import os
import requests
from tracker import fetch_transactions

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={"chat_id": CHAT_ID, "text": msg},
        timeout=30,
    )

try:
    tables = fetch_transactions()
    send(f"Sivulta löytyi {tables} HTML-taulukkoa.")
except Exception as e:
    send(str(e))