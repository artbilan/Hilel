import requests
from bs4 import BeautifulSoup


link = "https://lms.ithillel.ua"
response = requests.get(link)
if response.ok:
    response = response.text
    with open("link.html", "w", encoding="utf8") as file:
        file.write(response)

soup = BeautifulSoup(response, "lxml")
print(soup)
