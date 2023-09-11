import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from tests.test_pure import Test_pres

from selenium import webdriver
#from bs4 import BeautifulSoup
import pandas as pd
#テスト対象
#from web_scraping.gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from web_scraping.ruseki_mismatch import RuisekiMismatch
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
    rm = RuisekiMismatch()
    return rm


def read_test_data(test_file_path, test_file_name):
    data_df = Test_pres.data_read(test_file_path, test_file_name)
    return data_df


def test_mismatch_loanstump_rec_succes1():
    '''
        累積ファイルと逆日歩の不一致レコードの抽出テスト
        不一致レコード１件

            param
        ---------------
        None                                  :
            テスト対象クラス

            return
        ---------------
        ruiseki_df                                  : DataFrame
            不一致のみのデータフレーム
    '''
    rm = object_generate()
    gyaku_df = read_test_data(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_GYAKUHIBU_READ_FILE_NAME["succes1"]
    )
    ruiseki_df = read_test_data(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_RUIKEI_READ_FILE_NAME["succes1"]
    )
    result_df = rm.getMismatchLoanStumpRec(ruiseki_df, gyaku_df)
    result_df.to_csv(
        Test_const.TEST_FILE_PATH
        + Test_const.TEST_001_RESULT_FILE_NAME["succes1"]
    )
    succes_1_df = read_test_data(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_CORRECT_ANSWER_FILE_NAME["succes1"]
    )
    pd.testing.assert_frame_equal(left=result_df, right=succes_1_df)
    print("\n--succes1---")
    print(result_df)
    print(succes_1_df)


def test_mismatch_loanstump_rec_succes2():
    '''
        累積ファイルと逆日歩の不一致レコードの抽出テスト
        不一致レコード３件

            param
        ---------------
        None                                  :
            テスト対象クラス

            return
        ---------------
        ruiseki_df                                  : DataFrame
            不一致のみのデータフレーム
    '''
    rm = object_generate()
    gyaku_df = read_test_data(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_GYAKUHIBU_READ_FILE_NAME["succes1"]
    )
    ruiseki_df = read_test_data(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_RUIKEI_READ_FILE_NAME["succes2"]
    )
    result_df = rm.getMismatchLoanStumpRec(ruiseki_df, gyaku_df)
    result_df.to_csv(
        Test_const.TEST_FILE_PATH
        + Test_const.TEST_001_RESULT_FILE_NAME["succes2"]
    )
    succes_2_df = read_test_data(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_CORRECT_ANSWER_FILE_NAME["succes2"]
    )
    pd.testing.assert_frame_equal(left=result_df, right=succes_2_df)
    print("--succes2---")
    print(result_df)
    print(succes_2_df)
