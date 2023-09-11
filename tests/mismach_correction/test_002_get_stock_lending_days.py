import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from tests.test_pure import Test_pres

from selenium import webdriver
#from bs4 import BeautifulSoup
import pandas as pd
#テスト対象
#from web_scraping.gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from web_scraping.ruseki_mismatch import Ruiseki_mismach_correction
import pytest
#import pandas.testing.assert_frame_equal as a
from tests.test_const import Test_const


""" def test_driver_get():
    '''
    Chromedriverの環境設定

            param
        ---------------

            return
        ---------------
        driver                                  : object
            日経HTML取り込み済インスタンス
    '''
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"
    executable_path = driver_path + 'chromedriver_116'
    driver = webdriver.Chrome(executable_path, options=options)
    succes_companys_no = ['7211']
    driver.maximize_window()
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ succes_companys_no[0]
    driver.get(target_url)
    return driver """


def object_generate():
    '''
        Ruiseki_mismach インスタンスの生成

            param
        ---------------
        None                                  :
            テスト対象クラス

            return
        ---------------
        gt                                  : Object
            テスト対象インスタンス
    '''
    gt = Ruiseki_mismach_correction()
    return gt


def read_test_data(test_file_path, test_file_name):
    data_df = Test_pres.data_read(test_file_path, test_file_name)
    return data_df

def test_GetStockLendingDays_succes1():
    '''
        累積の累積貸株残が不一致の行から日付を抽出

            param
        ---------------
        None                                  :
            テスト対象クラス

            return
        ---------------
        ruiseki_df                                  : DataFrame
            不一致のみのデータフレーム
    '''
    gt = object_generate()
    ruiseki_df = read_test_data(Test_const.TEST_FILE_PATH,
                                Test_const.TEST_002_RUIKEI_READ_FILE_NAME)
    result_df = gt.getStocklendingDays(ruiseki_Non_stock_lending_df):
    """
    succes1_file_name = 'result_1_みずほフィナンシャルグループ_累積.csv'
    result_df.to_csv(Test_const.TEST_FILE_PATH + succes1_file_name)
    print(result_df)
    """
