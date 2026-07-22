import sqlite3

from datetime import datetime

DB = "tracker.db"

def init_db():

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    c.execute("""

    CREATE TABLE IF NOT EXISTS alerts (

        name TEXT,

        change REAL,

        date TEXT

    )

    """)

    conn.commit()

    conn.close()

def already_sent(name, change):

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    today = datetime.now().strftime("%Y-%m-%d")

    c.execute(

        "SELECT * FROM alerts WHERE name=? AND date=?",

        (name, today)

    )

    result = c.fetchone()

    conn.close()

    return result is not None

def save_alert(name, change):

    conn = sqlite3.connect(DB)

    c = conn.cursor()

    c.execute(

        "INSERT INTO alerts VALUES (?, ?, ?)",

        (

            name,

            change,

            datetime.now().strftime("%Y-%m-%d")

        )

    )

    conn.commit()

    conn.close()