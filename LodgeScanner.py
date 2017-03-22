# -*- coding: utf-8 -*-
import os
import time
import selenium.common.exceptions
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import traceback
import threading

__author__ = "Michael Yuan"
__copyright__ = "Copyright 2017"
__credits__ = "Catrina Meng"
__license__ = "GPL"
__version__ = "v1.0.1"


class LodgeScanner(object):

    def __init__(self):
        self.park = "gc"                        # Park Name (See run.py for example)
        self.year = "2017"
        self.month = "4"
        self.day = "9"
        self.method = "p"                       # Browser Option: PhantomJS or Chrome
        self.event = "hotel_update"             # Your IFTTT Trigger Event
        self.key = "cXlg9Sfft1nki7kUckYh64"     # Your IFTTT Maker Webhook Key
        self.count = 60                         # Notification Resend Count (Act as alarm clock...)

    def config(self, park, year, month, day, method):
        self.park = park
        self.year = year
        self.month = month
        self.day = day
        self.method = method

    def link_gen(self, park, year, month, day):
        link = "https://secure.[arg1].com/lodging/search?dateFrom=[arg2]&destination=ALL&preferred=&nights=1&adults=2&children=0&mtype=&promo=&member=&_ga=1.153607102.745836740.1490161045&datefrom=[arg2]"
        if park == "gc":
            arg1 = "grandcanyonlodges"
        elif park == "cl":
            arg1 = "craterlakelodges"
        elif park == "zp":
            arg1 = "zionlodge"
        elif park == "gp":
            arg1 = "glaciernationalparklodges"
        else:
            arg1 = "default"
        arg2 = month + "%2F" + day + "%2F" + year
        link = link.replace("[arg1]", arg1)
        link = link.replace("[arg2]", arg2)
        print link
        return link

    def check(self, page_source):
        soup = BeautifulSoup(page_source, 'html.parser')
        found = False
        if soup.find('div', id="hotel_results") is not None:
            result = soup.find_all('div', class_="no-availability")
            if result is None:
                return found
            print "<" + str(len(result)) + "> Lodges Retrieved:"
            block_list = soup.find_all('div', class_="container container-dark result isExpander")
            if block_list is not None:
                for block in block_list:
                    lodge_name = "<" + block.find('h4', class_="flt-left").string + ">"
                    if block.find('div', class_="no-availability") is not None:
                        print "Sold out: " + lodge_name
                    else:
                        info = lodge_name + " IS AVAILABLE NOW!!!"
                        print info
                        timestamp = time.strftime("%H:%M:%S", time.localtime())
                        if lodge_name != "<El Tovar Hotel>":
                            self.notify(self.event, self.key, info + timestamp, self.count)
                        found = True
        else:
            print "Web page does not contain room info."
        return found

    def post(self, event, key, info, count):
        link = "https://maker.ifttt.com/trigger/[event]/with/key/[key]"
        link = link.replace("[event]", event)
        link = link.replace("[key]", key)
        report = {}
        report["value1"] = info
        for x in range(0, count):
            requests.post(link, data=report)
            time.sleep(2)

    def notify(self, event, key, info, count):
        t = threading.Thread(target=self.post, name="notify-thread", args=(event, key, info, count))
        t.start()

    def run(self):
        # Create search link
        search_link = self.link_gen(self.park, self.year, self.month, self.day)
        # Begin Scanning
        while True:
            try:
                timestamp = time.strftime("%H:%M:%S", time.localtime())
                print timestamp
                # Select which browser to use
                if self.method == "p":
                    driver_path = os.getcwd() + "\\phantomjs.exe"
                    browser = webdriver.PhantomJS(executable_path=driver_path)
                else:
                    driver_path = os.getcwd() + "\\chromedriver.exe"
                    browser = webdriver.Chrome(executable_path=driver_path)
                browser.set_page_load_timeout(60)
                browser.get(search_link)
                self.check(browser.page_source)
            except selenium.common.exceptions.TimeoutException:
                print "Time out loading web page."
            except:
                print "Something goes wrong: " + traceback.format_exc()
            finally:
                browser.quit()
            print "---------------------------------------------------"
            time.sleep(60)          # Speed: 1 scan/min


