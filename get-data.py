from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup
import csv 

site = "http://www.achemenet.com/fr/item/?/sources-textuelles/textes-par-publication/Wunsch_CM_20/1328200"
page_html = Req(site).read()
pg_soup = soup (page_html, "html.parser")

