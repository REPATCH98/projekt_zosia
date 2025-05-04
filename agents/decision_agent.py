
import sqlite3
import time
from utils.gpt_utils import ask_gpt

def make_decisions():
    while True:
        print("Analizuję konwersacje do monetyzacji...")
        conn = sqlite3.connect('database/offers.db')
        cursor = conn.cursor()

        cursor.execute('SELECT id, user_message, zosia_response FROM interactions WHERE monetization_action = ""')
        interactions = cursor.fetchall()

        for interaction in interactions:
            id, user_message, zosia_response = interaction
            prompt = f"Rozmowa:\nUżytkownik: '{user_message}'\nZosia: '{zosia_response}'\nZaproponuj sposób monetyzacji (link, subskrypcja, usługa)."
            action = ask_gpt(prompt)

            cursor.execute('UPDATE interactions SET monetization_action = ? WHERE id = ?', (action, id))

        conn.commit()
        conn.close()
        print("Decyzje gotowe, czekam 180 sekund...")
        time.sleep(180)

if __name__ == "__main__":
    make_decisions()
