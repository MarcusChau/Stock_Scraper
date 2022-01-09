"""[summary]
This stock scraper uses Beautifulsoup library. 
Author: Marcus Chau
"""

from bs4 import BeautifulSoup  # import bs4 library
import requests  # import requests library
import time  # import time library


header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}

# stored ID equivalent to stock
ids = ['TSLA', 'AAPL', 'AMD', 'AMZN', 'FB', 'GOOGL', 'VTI']

# function stock
def get_stock():
    for id in ids:
        # obtaining URL
        url = f'https://finance.yahoo.com/quote/{id}'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'lxml')
        
        price = soup.find('div', class_='D(ib) Mend(20px)').text
        prev_close = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[0].text
        open_price = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[1].text
        year_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[5].text
        
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S %p", t)
        
        # writes information in TXT file
        with open(f'assets/{id}.txt', 'a') as f:
            f.write(f"{current_time}\n")
            f.write(f"Price: {price}\n")
            f.write(f"Previous Close: {prev_close}\n")
            f.write(f"Open Price: {open_price}\n")
            f.write(f"Year range: {year_range}\n")
            
            if ("09:30:00" < current_time < "04:00:01"):
                f.write("\n")
                continue
            else:
                change = soup.find('div', class_='Fz(12px) C($tertiaryColor) My(0px) D(ib) Va(b)').text
                day_range = soup.find_all('td', class_='Ta(end) Fw(600) Lh(14px)')[4].text
                
                f.write(f"Change after hours: {change}\n")
                f.write(f"Day range: {day_range}\n")
                f.write("\n")


if __name__ == '__main__':
    #while True:
        get_stock()
        #time_wait = 5
        #time.sleep(time_wait * 60)
