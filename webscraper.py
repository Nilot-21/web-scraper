import urllib.request
from bs4 import BeautifulSoup   

class Scraper:
    def __init__(self,site):
        self.site=site
    
    def scrape(self):

        retrieve=urllib.request.urlopen(self.site).read()
       
        sep=BeautifulSoup(retrieve,"html.parser")
        
        for art in sep.find_all("a"):
            url=art.get("href")
            if url is None:
                continue
            if "articles" in url:
                print("\n"+url)


news="https://news.google.com/"
Scraper(news).scrape()

