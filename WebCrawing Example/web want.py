from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.youtube.com")
bsObject = BeautifulSoup(html, "html.parser")

print (bsObject.head.find("meta",{"name":"description"}).get('content'))