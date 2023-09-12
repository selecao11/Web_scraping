import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from tests.test_pure import Test_pres

import pandas as pd
from web_scraping.ruseki_mismatch import RuisekiMismatch
import pytest
from tests.test_const import Test_const


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
    gt = RuisekiMismatch()
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
    ruiseki_Non_stock_lending_df = read_test_data(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_002_RUIKEI_READ_FILE_NAME["succes1"]
    )
    succes_1_df = ['2023-09-06']
    assert (gt.getStocklendingDays(ruiseki_Non_stock_lending_df) ==
            succes_1_df)

    print("\n--normal 1---")
    print("\n--input---")
    print(ruiseki_Non_stock_lending_df)
    ruiseki_Non_stock_lending_df
    print("\n--CORRECT_ANSWER---")
    print(succes_1_df)
