import requests
from bs4 import BeautifulSoup
import random



#response = requests.get("https://i-fakt.ru")
#response = response.content
#html = BeautifulSoup(response, "html.parser")#разбиваем код на теги
#print(html)
#facts = html.find_all(class_="p-2 clearfix")#к коду обращаться типо чтобы в список добавить только то что было в коде
#facts = random.choice(facts)#рандом факт

#print(facts)
#print(facts)
#print(facts[0].a.attrs)#только атрибут ссылки(норм ссылка)
#print(facts[0].a.attrs["href"])
#print(facts[0].a)#только структура ссылки, но не ссылка на факт
#print(facts[2].text)#выводит только текст факта

#print(facts.text)
#print(facts.a.attrs["href"])#выводит именно ссылку href


#post title

response = requests.get("https://kudago.com/msk/festival/")
response = response.content
html = BeautifulSoup(response, "html.parser")
#print(html)
fests = html.find_all(class_="post-title")#к коду обращаться типо чтобы в список добавить только то что было в коде

fest = random.choice(fests)#рандом факт
print(fest.text)
print(fest.a.attrs["href"])
#print(facts)
#print(facts)
#print(facts[0].a.attrs)#только атрибут ссылки(норм ссылка)
#print(facts[0].a.attrs["href"])
#print(facts[0].a)#только структура ссылки, но не ссылка на факт
#print(facts[2].text)#выводит только текст факта

#print(facts.text)
#print(facts.a.attrs["href"])#выводит именно ссылку href








