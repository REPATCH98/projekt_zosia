import threading
from agents.scraper_agent import scrape_lento
from agents.dialog_agent import start_conversations
from agents.decision_agent import make_decisions

if __name__ == "__main__":
    threading.Thread(target=scrape_lento).start()
    threading.Thread(target=start_conversations).start()
    threading.Thread(target=make_decisions).start()
