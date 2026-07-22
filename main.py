import os
import requests

from tracker import run_tracker
from insider import get_insider_buys


BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]


def send(msg):
    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id": CHAT_ID,
            "text": msg
        },
        timeout=30,
    )


try:
    messages = []

    market = run_tracker()

    if market:
        messages.append(market)


    insider = get_insider_buys()

    if insider:
        messages.append(
            "🦅 SISÄPIIRIOSTOT\n\n"
            + "\n".join(insider)
        )


    if messages:
        send("\n\n".join(messages))
    else:
        send("✅ Ei uusia sijoitushavaintoja.")


except Exception as e:
    send(f"❌ Tracker error:\n{e}")