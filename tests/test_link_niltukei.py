import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.kabuka import Kabuka
from web_scraping.gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from web_scraping.shinyou_zan import Shinyou_zan
from web_scraping.join import Join
from web_scraping.merge import Merge
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd
from selenium import webdriver


def test_driver_get():
    driver_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    executable_path = driver_path + 'chromedriver_116'
    driver = webdriver.Chrome(executable_path, options=options)
    succes_companys_no = ['7211']
    driver.maximize_window()
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ succes_companys_no[0]
    driver.get(target_url)
    return driver

def test_niltukei_succes1():
    driver = test_driver_get()
    kb = Kabuka()
    file_path = './'
    file_name = '_link_株価.csv'
    kb.kabuka_title_get(driver)
    kb.kabuka_taisyaku_init_set(file_name,file_path)
    kb.kabuka_df_cleate(WebDriverWait,driver,pd,By,file_path,file_name)
    print("ok")

    gt = Gyakuhibu_taisyaku()
    file_path = './'
    file_name = '_link_逆日歩_貸借桟.csv'
    gt.gyakuhibu_taisyaku_title_get(driver)
    gt.gyakuhibu_taisyaku_init_set(file_name,file_path)
    gt.gyakuhibu_taisyaku_df_cleate(WebDriverWait,driver,pd,By)

    sz = Shinyou_zan()
    file_path = './'
    file_name = '_link_信用残.csv'
    sz.shinyou_zan_title_get(driver)
    sz.shinyou_zan_init_set(file_name,file_path)
    sz.shinyou_zan_df_cleate(WebDriverWait,driver,pd,By)

    csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"
    join_kabuka_df = pd.read_csv(csv_path +'tests/三菱自動車_link_株価.csv')
    join_shinyou_zan_df = pd.read_csv(csv_path + 'tests/三菱自動車_link_信用残.csv')
    join_gyakuhibu_taisyaku_df = pd.read_csv(csv_path + 'tests/三菱自動車_link_逆日歩_貸借桟.csv')

    jb = Join()
    jb.nikei_join_init(join_kabuka_df,join_shinyou_zan_df,join_gyakuhibu_taisyaku_df)
    nikei_join_df = jb.nikei_jion()
    nikei_join_df.to_csv(csv_path + 'tests/三菱自動車_link_株価_信用残_逆日歩_貸借桟.csv')

    ruiseki_df = pd.read_csv(csv_path + '/tests/三菱自動車_累積.csv')
    nikei_data_df = pd.read_csv(csv_path + '/tests/三菱自動車_link_株価_信用残_逆日歩_貸借桟.csv')
    mg = Merge()
    mg.nikei_merge_init(ruiseki_df,nikei_data_df)
    merge_df = mg.nikei_merge()
    merge_df.to_csv(csv_path + '/tests/三菱自動車_link_マージ.csv')
