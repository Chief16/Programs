import requests
import urllib3
import time
from __constants.constants import *
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main():

    last_l = len(chk_list)

    while True:
        for index, url in enumerate(chk_list):
            r = requests.get(url, headers=head, verify=False)
            soup = BeautifulSoup(r.content, 'html.parser')

            try:
                if soup.find('button', class_='a-button-text').text == 'See All Buying Options':
                    name = soup.find('span', id_='productTitle').text
                    print(f'{name} is out of stock')
                    if index == last_l - 1:
                        time.sleep(10)

            except:
                if soup.find('button', class_='a-button-input').text == 'Add to Shopping Cart':
                    name = soup.find('span', id_='productTitle').text
                    print(f'{name} is in stock')
                    if index == last_l - 1:
                        time.sleep(10)

if __name__ == '__main__':
    main()


