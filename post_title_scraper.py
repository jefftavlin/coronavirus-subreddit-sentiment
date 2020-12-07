import requests
import csv
import time
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
import pandas as pd

url = 'https://www.reddit.com/r/Coronavirus'

def open_page(url, pages = 0):
    chrome_options = webdriver.ChromeOptions()
    
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)
    driver = webdriver.Chrome('C:\Program Files (x86)\chromedriver.exe',options = chrome_options)
    
    driver.get(url)
    post_titles = []
    
    if pages > 0:
        for i in range(pages):
            driver.execute_script(f"window.scrollTo(0, document.body.scrollHeight)")
            time.sleep(0.3)
            search = driver.find_elements_by_class_name('_eYtD2XCVieq6emjKBH3m')
            for element in search:
                post_titles.append(element.text)
    
    bad_items = ['About Community','Filter by flair','Useful Resources:','r/Coronavirus Rules','Related communities','Region-Specific Subreddits',
                'More regional subreddits','Moderators','']
    post_titles = [post for post in post_titles if post not in bad_items]
            
    time.sleep(1)
    driver.quit()
    
    return post_titles
    
posts = open_page(url,100)
df = pd.DataFrame(posts, columns = ['Post_title'])
df.to_csv('reddit_titles.csv')
