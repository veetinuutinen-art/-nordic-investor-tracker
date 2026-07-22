import yfinance as yf
from datetime import datetime


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

    alerts = []

    for name, ticker in WATCHLIST.items():

        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period="2d")

            if len(data) < 2:
                continue

            old = data["Close"].iloc[0]
            new = data["Close"].iloc[-1]

            change = ((new - old) / old) * 100

            if abs(change) >= 2:
                emoji = "📈" if change > 0 else "📉"

                alerts.append(
                    f"{emoji} {name}\n"
                    f"{change:.2f}%\n"
                    f"Hinta: {new:.2f}"
                )

        except Exception:
            continue


    if alerts:
        return (
            "📊 Nordic Investor Tracker\n\n"
            + "\n\n".join(alerts)
            + f"\n\n⏱ {datetime.now().strftime('%d.%m.%Y %H:%M')}"
        )

    return None