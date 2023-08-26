from gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.chrome.options import Options
import pandas as pd
from selenium import webdriver
#from bs4 import BeautifulSoup

def test_driver_get():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    executable_path = '/home/user/anaconda3/envs/Web_scraping/source/test/chromedriver_114'
    driver = webdriver.Chrome(executable_path, options=options)
    succes_companys_no = ['7211']
    driver.maximize_window()
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ succes_companys_no[0]
    driver.get(target_url)
    return driver

def test_shinyou_zan_succes1():
    driver = test_driver_get()
    gt = Gyakuhibu_taisyaku()
    gt.gyakuhibu_taisyaku_title_get(driver)
    file_path = './'
    file_name = '_逆日歩_貸借桟_.csv'
    gt.gyakuhibu_taisyaku_init_set(file_name,file_path)
    gt.gyakuhibu_taisyaku_df_cleate(WebDriverWait,driver,pd,By)
