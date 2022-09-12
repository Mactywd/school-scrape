import requests
from bs4 import BeautifulSoup
import telegram_send


def main():
    page = requests.get("https://galilei.edu.it/", headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(page.content, "html.parser")
    tag = soup.find_all("a", class_="wp-block-navigation-item__content")[1]
    
    if tag.text != "Orario scolastico 2021":
        
        url = tag["href"]
        telegram_send.send(messages=["It updated!", url])

if __name__ == '__main__':
    main()