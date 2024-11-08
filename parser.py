import requests
from bs4 import BeautifulSoup
import json

def quotes_to_scrape():
    quotes = []
    page_number = 1

    while True:
        url = f'https://quotes.toscrape.com/page/{page_number}/'
        response = requests.get(url)

        soup = BeautifulSoup(response.text, 'html.parser')

        for quote in soup.find_all('div', class_='quote'):
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            quotes.append({'text': text, 'author': author, 'tags': tags})
        next_page = soup.find('li', class_='next')
        if not next_page:
            break

        page_number += 1

    with open('quotes.json', 'w', encoding='utf-8') as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

quotes_to_scrape()