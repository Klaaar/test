import requests
from bs4 import BeautifulSoup
import random

def get_facts():
    response = requests.get("https://afisha.yandex.ru/kostroma/concert")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_ = "Title-fq4hbj-3"))
    print(fact.text)

get_facts()


