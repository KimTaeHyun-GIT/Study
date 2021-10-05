import requests
from bs4 import BeautifulSoup

url = "http://shop.danawa.com/virtualestimate/?controller=estimateMain&methods=index&marketPlaceSeq=16&logger_kw=dnw_gnb_esti"
res = requests.get(url)
res.raise_for_status()

print(len(res.text))
print(res.text)

