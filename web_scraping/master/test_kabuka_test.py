#from kabuka import Kabuka
import requests
#from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#import pandas as pd
from selenium import webdriver
#import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

'''def test_driver_get():
    options = Options()
    driver = webdriver.Chrome(options=options)
    succes_companys_no = ['7211']
    #driver = webdriver.Chrome()
    driver.maximize_window()
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ succes_companys_no
    #soup = BeautifulSoup(target_url,'html.parser')
    driver.get(target_url)
    return driver'''
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options = Options()
#options.add_argument('--headless')
def test_driver_get():
    succes_companys_no = ['7211']
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # ダウンロード先のpath情報を指定
    #executable_path = '/Users/myname/Downloads/chromedriver'
    executable_path = '/home/user/anaconda3/envs/Web_scraping/chromedriver'
    driver = webdriver.Chrome(executable_path, options=options)
    #driver.get("https://www.selenium.dev/selenium/web/web-form.html")
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ succes_companys_no[0]
    driver.get(target_url)
    return driver 

def test_kabuka_succes1():
    driver = test_driver_get()
#    kb =   Kabuka()
#    kb_title = kb.kabuka_title_get(driver)
#    file_path = './'
#    file_name = kb_title + '_株価_.csv'
    print("okok")
    #kb.kabuka_df_cleate((WebDriverWait,driver,pd,By,file_path,file_name))
    '''print("\n")
    print("succes_companys_no")
    pprint.pprint(succes_companys_no,width=100,compact=True)
    print("test_companys_no")
    pprint.pprint(test_companys_no,width=100,compact=True)
    assert succes_companys_no == test_companys_no'''

test_kabuka_succes1()
