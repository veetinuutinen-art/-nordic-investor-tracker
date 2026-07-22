import yfinance as yf
from datetime import datetime
from database import init_db, already_sent, save_alert


WATCHLIST = {
    "Nokia": "NOKIA.HE",
    "Sampo": "SAMPO.HE",
    "Kone": "KNEBV.HE",
    "Neste": "NESTE.HE",
    "Fortum": "FORTUM.HE",
    "Volvo": "VOLV-B.ST",
    "Investor AB": "INVE-B.ST",
    "Saab": "SAAB-B.ST",
    "Novo Nordisk": "NOVO-B.CO"
}


def run_tracker():

    init_db()

    alerts = []

    for name, ticker in WATCHLIST.items():

        stock = yf.Ticker(ticker)
        data = stock.history(period="2d")

        if len(data) < 2:
            continue

        old = data["Close"].iloc[0]
        new = data["Close"].iloc[-1]

        change = ((new-old)/old)*100

        if abs(change) >= 2:

            if already_sent(name, round(change,2)):
                continue

            save_alert(name, round(change,2))

            emoji = "📈" if change > 0 else "📉"

            alerts.append(
                f"{emoji} {name}\n"
                f"{change:.2f}%\n"
                f"Hinta: {new:.2f}"
            )


    if alerts:
        return (
            "📊 Nordic Investor Tracker\n\n"
            + "\n\n".join(alerts)
            + "\n\n⏱ "
            + datetime.now().strftime("%d.%m.%Y %H:%M")
        )

    return None