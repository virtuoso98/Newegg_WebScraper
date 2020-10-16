from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup
import csv 

base = "http://www.achemenet.com/"
accumulator = []


# parsing for website name begins. Here we go! 
for index in range (1, 11) :
    head, tail = "http://www.achemenet.com/fr/tree/?/sources-textuelles/textes-par-publication/Wunsch_CM_20/" , "/24/0#set"
    site = head + str(index) + tail
    page_html = Req(site).read()
    pg_soup = soup (page_html, "html.parser")
    for product in pg_soup.find_all("div", class_ = "item"):
        target = base + product.find("a").get('href')
        accumulator.append(target)
    