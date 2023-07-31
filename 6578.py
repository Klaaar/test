#зацикливание
#number =10
#while number < 100:
 #   number += 50
  #  print(number)

import requests
from bs4 import BeautifulSoup
import random

#def get_facts():
#    response = requests.get("https://afisha.yandex.ru/kostroma/concert")
#    response = response.content
#    html = BeautifulSoup(response, "html.parser")
#    fact = random.choice(html.find_all(class_ = "Root-fq4hbj-4 iFrhLC"))
#    print(fact.text)
#    print(fact.a.attrs["href"])

#def get_concert():
#     response = requests.get("https://kudago.com/msk/concerts/")
#     response = response.content
#     html = BeautifulSoup(response, "html.parser")
#     fact = random.choice(html.find_all(class_ = "post-title"))
#     print(fact.text)
#     print(fact.a.attrs["href"])

#user_wish = ""

#while user_wish != "Хватит":
#    user_wish = input("Чем заняться?")
#    if user_wish == "факт":
#        get_facts()
#    else:
#        get_concert()
#    #else:
#       # print("А нормально?")





















