from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}


work = Session()

work.get("https://quotes.toscrape.com/", headers=headers)

responce = work.get("https://quotes.toscrape.com/login", headers=headers)

soup = BeautifulSoup(responce.text, "lxml")

token = soup.find("form").find("input").get("value")

data = {"csrf_token": token,
"username": "noname",
"password": "password"}

result = work.post("https://quotes.toscrape.com/login", headers=headers, data=data, allow_redirects=True)
