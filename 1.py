import requests
from bs4 import BeautifulSoup

response = requests.get("http://www.columbia.edu/~fdc/sample.html")
response = response.content
html = BeautifulSoup(response, "html.parser")
h3 = html.find_all("h3")

print(h3)








