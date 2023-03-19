import requests

URL = "https://coinmarketcap.com/"

res = requests.get(URL)

print(res.text)