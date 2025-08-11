#//*[@id="constituents"]/tbody/tr[2]/td[1]
#//*[@id="main-content-wrapper"]/section[1]/div[2]/div[1]/section/div/section/div[1]/div[1]/span
#//span[contains(@data-testid,"qsp-price")]/text()

import requests
from bs4 import BeautifulSoup
import time
from lxml import html
import yfinance as yf
from threading import *
from multiprocessing import Queue



def extract_data(response_text):
    
    soup = BeautifulSoup(response_text,"html.parser")
    results = list(soup.find("tbody"))[1:]
    results_set = list(set(results)- set("\n"))
    print("total result is ",len(results_set));print("last element is ",results_set[-1])
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


class YahooFinancePriceScheduler(Thread):
    def __init__(self,input_queue,**kwargs):
        super(YahooFinancePriceScheduler,self).__init__(**kwargs)
        self._input_queue = input_queue
        self.start()
    
    def run(self):
        while True:
            if self._input_queue.get() != 'DONE':
                symbol = self._input_queue.get()
                # print("Symbol is ",symbol)
                try:
                    ticker = yf.Ticker(symbol)
                except KeyError as e:
                    key_issue = f'{symbol} - {e}'
                    print(key_issue)
                except requests.exceptions.HTTPError as e:
                    print("HTTP Error -> ",e)
                else:
                    # Get the current price and other key info
                    stock_info = ticker.info

                    # Print some key data
                    if 'currentPrice' in stock_info.keys():
                        print(f"Current Price: {stock_info['currentPrice']} USD")
                    else:
                        pass
            else:
                break


if __name__ == "__main__":
    base_url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    current_workers = []
    symbol_queue = Queue()
    num_yahoo_workers = 5
    yahoo_wrokers = []
    for i in range(num_yahoo_workers):
        yahoofinpricesched = YahooFinancePriceScheduler(input_queue=symbol_queue)
        yahoo_wrokers.append(yahoofinpricesched)

    start_time = time.time()
    for symbol in get_sp_500_company_data(base_url):
        
        symbol_queue.put(symbol)
    
    for i in range(num_yahoo_workers):
        symbol_queue.put("DONE")

    for i in range(num_yahoo_workers):
        yahoo_wrokers[i].join()

    
        
        
    end_time = time.time()

    print("total time ",end_time-start_time)
    print("total threads is ",len(current_workers))





    