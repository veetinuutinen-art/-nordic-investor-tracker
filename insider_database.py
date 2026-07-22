import sqlite3

DB = "insider.db"


def init_insider_db():
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute("""
    CREATE TABLE IF NOT EXISTS insider_alerts (
        company TEXT,
        alert TEXT
    )
    """)

    conn.commit()
    conn.close()


def already_seen(company, alert):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "SELECT * FROM insider_alerts WHERE company=? AND alert=?",
        (company, alert)
    )

    result = c.fetchone()

    conn.close()

    return result is not None


def save_seen(company, alert):
    conn = sqlite3.connect(DB)
    c = conn.cursor()

    c.execute(
        "INSERT INTO insider_alerts VALUES (?,?)",
        (company, alert)
    )

    conn.commit()
    conn.close()