import requests

from bs4 import BeautifulSoup

URL = "https://coinmarketcap.com/"

res = requests.get(URL)

if res.status_code == 200:
  soup = BeautifulSoup(res.text, features="html.parser")
  info = soup.find_all("a", {"href":"/currencies/bitcoin/markets/"})
  price = info[0].getText()
  print(price)
  
  info = soup.find_all("p", {"class":"sc-e225a64a-0 ePTNty"})
  name = info[0].getText()
  print(name)
  
  info = soup.find_all("a", {"href":"/currencies/ethereum/markets/"})
  price = info[0].getText()
  print(price)
  
  info = soup.find_all("p", {"class":"sc-e225a64a-0 ePTNty"})
  name = info[0].getText()
  print(name)
  
  info = soup.find_all("a", {"href":"/currencies/tether/markets/"})
  price = info[0].getText()
  print(price)






