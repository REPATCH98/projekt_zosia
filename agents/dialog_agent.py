
import sqlite3
import time
from utils.gpt_utils import ask_gpt

def start_conversations():
    while True:
        print("Sprawdzam nowe oferty do konwersacji...")
        conn = sqlite3.connect('database/offers.db')
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS interactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            offer_id INTEGER,
            user_message TEXT,
            zosia_response TEXT,
            monetization_action TEXT,
            FOREIGN KEY (offer_id) REFERENCES offers(id)
        )""")

        cursor.execute('SELECT id, title FROM offers')
        offers = cursor.fetchall()

        for offer in offers:
            offer_id, title = offer
            user_message = f"Cześć, interesuje mnie oferta: {title}. Powiedz coś więcej."

            prompt = f"Wciel się w rolę kobiety o imieniu Zosia. Odpowiedz uprzejmie na: '{user_message}'"
            zosia_response = ask_gpt(prompt)

            cursor.execute('INSERT INTO interactions (offer_id, user_message, zosia_response, monetization_action) VALUES (?, ?, ?, ?)',
                           (offer_id, user_message, zosia_response, ''))

        conn.commit()
        conn.close()
        print("Zosia odpowiedziała, czekam 120 sekund...")
        time.sleep(120)

if __name__ == "__main__":
    start_conversations()
