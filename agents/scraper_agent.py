
import requests
from bs4 import BeautifulSoup
import sqlite3
import time

def scrape_lento():
    while True:
        print("Scraping Lento...")
        response = requests.get("https://lento.pl/oferty/")
        soup = BeautifulSoup(response.text, "html.parser")
        offers = soup.select(".title-list-item")

        conn = sqlite3.connect('database/offers.db')
        cursor = conn.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            description TEXT,
            category TEXT,
            link TEXT
        )""")

        for offer in offers:
            title = offer.get_text(strip=True)
            link = offer['href']
            cursor.execute('INSERT INTO offers (title, description, category, link) VALUES (?, ?, ?, ?)',
                           (title, 'Opis niedostępny', 'Nieznana', link))

        conn.commit()
        conn.close()
        print("Scraping zakończony, czekam 60 sekund...")
        time.sleep(60)

if __name__ == "__main__":
    scrape_lento()
