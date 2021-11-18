import requests
from bs4 import BeautifulSoup

url = "https://rozetka.com.ua/ua/sport-i-uvlecheniya/c4627893/"
response_text = ""

response = requests.get(url) # comment
if response.ok == True:
    response_text = response.text

soup = BeautifulSoup(response_text, "lxml")

find_url = soup.find_all(class_="tile-cats__heading ng-star-inserted")
# print(find_url) # Задача №1

url_dict = {}
new_list = []

find_url2 = soup.find_all(class_="portal-grid__cell ng-star-inserted")
for i in find_url2:
    new_list.append(i.text)

for i in find_url:
    url_dict.update({i.get("title"):i.get("href")})

for i, v in url_dict.items():
    print(i, v) # Задача №2

# print(new_list) # Добавить этот список к ключам с задания №2 не получается.

