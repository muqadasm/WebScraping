import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/page/"

with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["quote_title", "quote_author", "quote_tag"])

    for page in range(1, 51):

        response = requests.get(url + str(page))

        soup = BeautifulSoup(response.text, 'html.parser')

        quotes = soup.find_all('div', class_='quote')

        if not quotes:
            print("No more pages to scrape.")
            break

        for quote in quotes:
            quote_title = quote.find('span', {'class':'text'}).get_text()
            quote_author = quote.find('small', {'class':'author'}).get_text()
            quote_tags = quote.find_all('a', {'class':'tag'})

            quote_tag = ([tag.get_text() for tag in quote_tags])

            writer.writerow([quote_title, quote_author, quote_tag])

            print(quote_title)
            print("Author:", quote_author)
            print("Tags:", quote_tag)
