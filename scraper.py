# scraper.py
import requests
from bs4 import BeautifulSoup

def scrape_sample():
    url = "https://example.com"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    print("Scraping done (sample)")
    return True
