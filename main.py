import requests

from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Comfortable-Ergonomic-Computer-Cockpit-Simulator/dp/B0BPSV8L7H/ref=sr_1_7?keywords=gaming+chairs&pd_rd_r=a733c5d2-0f21-4e46-a37c-085332472b71&pd_rd_w=V5jej&pd_rd_wg=tGhjq&pf_rd_p=12129333-2117-4490-9c17-6d31baf0582a&pf_rd_r=MBWWPYNYVJRXGRMZQ8GE&qid=1679212809&sr=8-7"

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






