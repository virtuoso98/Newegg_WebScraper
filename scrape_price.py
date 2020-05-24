from urllib.request import urlopen as Req
from bs4 import BeautifulSoup as soup
import csv 
import datetime

url = "https://www.newegg.com/p/pl?N=100007709%20600030348%204814&page=1"

# connecting to website
urlreq = Req(url)
page_html = urlreq.read()

# parsing begins. some prototyping code for single website
acc = {}
pg_soup = soup (page_html, "html.parser")
product_page = pg_soup.find("div", class_ = 'item-container')

# creation of csv file

time_now = datetime.datetime.now().strftime("%d-%m-%Y")
filename = time_now + "nvidia-px.csv"
f = open (filename, "w", encoding = "utf-8")
headers = "brand, product, price, shipping, hyperlink\n"
f.write (headers)

# scraping for 30 websites

for index in range (1,21):
    template = "https://www.newegg.com/p/pl?N=100007709%20600030348%204814&page="
    site = template + str (index)
    page_html = Req(site).read()
    pg_soup = soup (page_html, "html.parser")
    i = 0
    for product in pg_soup.find_all("div", class_ = 'item-container'):
        
        try : 
            brand = product.find("a", class_ = "item-brand").img["title"]
        except Exception as e: 
            brand = "None"

        gfx = product.find("a", class_ = "item-title").text.strip("\xa0")
        raw_price = product.find("li", class_ = "price-current").text

        price = (raw_price.strip().split("\xa0"))[0]

        shipping = (product.find("li", class_ = "price-ship").text).strip().strip("\xa0")

        # hyperlink to product website
        link = product.a["href"]

        # prevent commas from variables disrupting csv file
        f.write (brand.replace(",", " ") + "," + gfx.replace(",", "|") + "," + price.replace(",", "") + "," + shipping + "," + link + "\n")
        
f.close()
