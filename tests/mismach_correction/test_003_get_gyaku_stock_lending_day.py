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


def readDataFrame(test_file_path, test_file_name):
    data_df = Test_pres.readDataFrame(test_file_path, test_file_name)
    return data_df


def testGetGyakuStockLendingDay_normal_1():
    '''
        逆日歩_貸株残から貸株残が不一致の日を抽出

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
    # --入力ファイル--
    # ---逆日歩---
    GetGyakuStockLendingDay_gyaku_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_GYAKUHIBU_READ_FILE_NAME["normal_1"]
    )
    # ---累積---
    GetGyakuStockLendingDay_ruiseki_pd = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_003_RUIKEI_READ_FILE_NAME["normal_1"]
    )
    # ---正解---
    GetGyakuStockLendingDay_succes_1_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_003_CORRECT_ANSWER_FILE_NAME["normal_1"]
    )

    # --テスト実施--
    GyakuStockLendingDay_pd = gt.GetGyakuStockLendingDay(
        GetGyakuStockLendingDay_ruiseki_pd,
        GetGyakuStockLendingDay_gyaku_df
    )

    # 処理結果出力CSVファイル出力
    # --逆日歩不一致日付出力--
    GyakuStockLendingDay_pd.to_csv(
            Test_const.TEST_FILE_PATH
            + Test_const.TEST_003_RESULT_FILE_NAME["normal_1"]
    )

    print("\n★★★★ normal 1★★★★")
    print("\n--normal 1 input 1---")
    print(GetGyakuStockLendingDay_ruiseki_pd)
    print("\n--normal 1 input 2---")
    print(GetGyakuStockLendingDay_gyaku_df)
    print("\n--normal 1 CORRECT_ANSWER---")
    print(GetGyakuStockLendingDay_succes_1_df)
    print("\n--normal 1 RESULT_FILE---")
    print(GyakuStockLendingDay_pd)

    # --テスト確認--
    pd.testing.assert_frame_equal(
        left=GyakuStockLendingDay_pd,
        right=GetGyakuStockLendingDay_succes_1_df)
