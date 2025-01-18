import csv
from bs4 import BeautifulSoup
import requests

url = "https://books.toscrape.com/catalogue/page-"

with open('book.csv', mode='w', newline='', encoding='utf_8') as file:
    writer = csv.writer(file)
    writer.writerow(['Book Title', 'Book Price', 'Book Description'])

    for page in range(1, 51):
        response = requests.get(url + str(page) + '.html')
        soup = BeautifulSoup(response.text, 'html.parser')

        books = soup.find_all('article', {'class': 'product_pod'})

        for book in books:
            book_title = book.find('h3').find('a')['title']
            book_price = book.find('p', {'class': 'price_color'}).text

            books_url = book.find('h3').find('a')['href']
            book_url = "https://books.toscrape.com/catalogue/" + books_url

            book_page = requests.get(book_url)
            soup = BeautifulSoup(book_page.text, 'html.parser')

            try:
                description_section = soup.find('meta', {'name': 'description'})['content']
            except TypeError:
                description_section = 'No description available'

            writer.writerow([book_title, book_price, description_section])

print("Data has been saved.")
