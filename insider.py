import requests
from datetime import datetime


def get_insider_buys():

    alerts = []

    sources = [
        {
            "country": "Finland",
            "url": "https://www.inderes.fi"
        },
        {
            "country": "Sweden",
            "url": "https://www.fi.se"
        },
        {
            "country": "Denmark",
            "url": "https://www.finanstilsynet.dk"
        },
        {
            "country": "Norway",
            "url": "https://www.finanstilsynet.no"
        }
    ]

    # Pohja eri maiden ilmoitusten keräämiselle
    # Varsinaiset API-haut lisätään seuraavaksi

    if alerts:
        return alerts

    return []