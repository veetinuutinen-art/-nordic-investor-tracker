import os

import requests

BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]

CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

message = """🚀 Nordic Investor Tracker

Jos saat tämän viestin, kaikki toimii!

Seuraavaksi alamme seurata:

🇫🇮 Suomi

🇸🇪 Ruotsi

🇳🇴 Norja

🇩🇰 Tanska

Terveisin,

Nordic Investor Tracker"""

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

response = requests.post(

    url,

    data={

        "chat_id": CHAT_ID,

        "text": message

    },

    timeout=30

)

print(response.text)