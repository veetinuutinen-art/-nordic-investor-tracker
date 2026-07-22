import requests
from bs4 import BeautifulSoup
from datetime import datetime

print("=" * 50)
print("Nordic Investor Tracker")
print("Käynnistyy:", datetime.now())
print("=" * 50)

sources = [
    {
        "name": "Finansinspektionen Sweden",
        "url": "https://www.fi.se"
    },
    {
        "name": "Nasdaq Nordic",
        "url": "https://www.nasdaq.com"
    }
]

for source in sources:
    try:
        response = requests.get(source["url"], timeout=10)
        print(f"✅ {source['name']} - OK ({response.status_code})")
    except Exception as e:
        print(f"❌ {source['name']} - {e}")

print("\nTracker toimii.")
