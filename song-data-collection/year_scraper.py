import pandas as pd
import translators as ts
import translators.server as tss
import json
import random
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from lxml import html
import json
import requests
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


song_dict = None
with open("5. output.json",'r') as json_file:
    song_dict = json.load(json_file)


def SaveHTML(yt_link,i):
    driver = webdriver.Edge()
    driver.get(yt_link)
    soup = BeautifulSoup(driver.page_source)
    page_source  = soup.find('body').prettify()
    with open("html_dumps/"+str(i)+".html",'w',encoding='UTF-8') as f:
        f.write(page_source)
    print("Completed : "+yt_link)

i=0
for song in song_dict:
    yt_link = song["youtube_link"]
    SaveHTML(yt_link,i)
    i+=1
    break