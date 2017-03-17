# -*- coding: utf-8 -*-
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
from datetime import datetime

__author__ = "Michael Yuan"
__copyright__ = "Copyright 2017"
__credits__ = "Catrina Meng"
__license__ = "GPL"
__version__ = "v0.0.1"


def check(page_source):
    soup = BeautifulSoup(page_source, 'html.parser')
    found = False
    print "[" + str(datetime.now().time()) + "]"
    if soup.find('div', id="hotel_results") is not None:
        result = soup.find_all('div', class_="no-availability")
        if len(result) == 5:
            print "Shit!"
        else:
            print "Awesome! Lodge available! Get up and book it!!!"
        block_list = soup.find_all('div', class_="container container-dark result isExpander")
        if block_list is not None:
            for block in block_list:
                lodge_name = "<" + block.find('h4', class_="flt-left").string + ">"
                if block.find('div', class_="no-availability") is not None:
                    print lodge_name + " sold out."
                else:
                    print lodge_name + " IS AVAILABLE NOW!!!"
                    notify(lodge_name + " IS AVAILABLE NOW!!!")
                    found = True
    else:
        print "Web page does not contain room info."
    return found


def notify(info):
    report = {}
    report["value1"] = info
    requests.post("https://maker.ifttt.com/trigger/hotel_update/with/key/cXlg9Sfft1nki7kUckYh64", data=report)


test = os.getcwd() + "\\test.html"
driver_path = os.getcwd() + "\\phantomjs.exe"
driver_path2 = os.getcwd() + "\\chromedriver.exe"
#search_link = "https://secure.grandcanyonlodges.com/lodging/search?dateFrom=04%2F28%2F2017&destination=ALL&preferred=&nights=1&adults=2&children=0&mtype=&promo=&member=&_ga=1.149685747.414995150.1489741882&datefrom=04%2F28%2F2017&dateTo=04%2F29%2F2017&dateto=04%2F29%2F2017"
search_link = "https://secure.grandcanyonlodges.com/lodging/search?dateFrom=04%2F09%2F2017&destination=ALL&preferred=&nights=1&adults=2&children=0&mtype=&promo=&member=&_ga=1.86919963.2022048644.1489410486&datefrom=04%2F09%2F2017&dateTo=04%2F10%2F2017&dateto=04%2F10%2F2017"

count = 0
status = False
while True:
    count += 1
    browser = webdriver.PhantomJS(executable_path=driver_path)
    #browser = webdriver.Chrome(executable_path=driver_path2)
    browser.set_page_load_timeout(60)
    try:
        browser.get(search_link)
        status = status or check(browser.page_source)
    except:
        print "Time out loading web page."
    finally:
        browser.quit()
    print "---------------------------------------------------"
    if (count == 30):
        if status:
            notify("Found available rooms! Please check it out ASAP.")
        else:
            notify("No available rooms during this hour.")
        count = 0
    time.sleep(60)

