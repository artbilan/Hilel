import requests

link = "https://www.kissfm.ua/"
response = requests.get(link)
print(response)

if response.ok:
    response = response.text
    print(response)