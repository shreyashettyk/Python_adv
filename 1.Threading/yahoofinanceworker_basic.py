#//*[@id="constituents"]/tbody/tr[2]/td[1]
#//*[@id="main-content-wrapper"]/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span
#//span[contains(@data-testid,"qsp-price")]/text()

import requests
from bs4 import BeautifulSoup
import time
from lxml import html
import yfinance as yf
from threading import *

def extract_data(response_text):
    
    soup = BeautifulSoup(response_text,"html.parser")
    results = list(soup.find("tbody"))[1:]
    results_set = list(set(results)- set("\n"))
    print("total result is ",len(results_set))
    for each_record in results_set:
        symbol = each_record.find("a").text
        yield symbol
        
def get_sp_500_company_data(url_link):
    try:
        resp = requests.get(url = url_link)
    except requests.ConnectionError  as e:
        print(e)
    else:
        yield from extract_data(resp.text)


class YahooFinanceWorker(Thread):
    def __init__(self,symbol,**kwargs):
        super(YahooFinanceWorker,self).__init__(**kwargs)
        self._symbol = symbol
        self.start()
    
    def run(self):
        try:
            ticker = yf.Ticker(symbol)
        except KeyError as e:
            key_issue = f'{symbol} : {e}'
            print(key_issue)
        else:
            # Get the current price and other key info
            stock_info = ticker.info

            # Print some key data
            print(f"Current Price: {stock_info['currentPrice']} USD")


if __name__ == "__main__":
    base_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    current_workers = []
    start_time = time.time()
    for symbol in get_sp_500_company_data(base_url):
        print(symbol)
        yahoofinpriceworker = YahooFinanceWorker(symbol = symbol)
        current_workers.append(yahoofinpriceworker)
    
    for i in range(len(current_workers)):
        current_workers[i].join()
        
        
        
    end_time = time.time()

    print("total time ",end_time-start_time)
    print("total threads is ",len(current_workers))





    