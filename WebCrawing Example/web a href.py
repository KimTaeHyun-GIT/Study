from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.naver.com")
bsObject = BeautifulSoup(html, "html.parser")

for link in bsObject.head.find_all('a'):
    print(link.get.strip(), link.get('href'))