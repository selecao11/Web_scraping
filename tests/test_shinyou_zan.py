import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.shinyou_zan import Shinyou_zan
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium import webdriver
#from bs4 import BeautifulSoup

def test_driver_get():
    driver_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    executable_path = driver_path + 'chromedriver_116'
    #executable_path = '/home/user/anaconda3/envs/Web_scraping/source/test/chromedriver_114'
    driver = webdriver.Chrome(executable_path, options=options)
    succes_companys_no = ['7211']
    driver.maximize_window()
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ succes_companys_no[0]
    driver.get(target_url)
    return driver
    #options = Options()
    #driver = webdriver.Chrome(options=options)
    #driver = webdriver.Chrome()
    #soup = BeautifulSoup(target_url,'html.parser')

def test_shinyou_zan_succes1():
    driver = test_driver_get()
    sz = Shinyou_zan()
    file_path = './'
    file_name = '_信用残.csv'
    sz.shinyou_zan_title_get(driver)
    sz.shinyou_zan_init_set(file_name,file_path)
    sz.shinyou_zan_df_cleate(WebDriverWait,driver,pd,By)
