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
    SetStockLendingRuisekiDay_gyaku_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_004_GYAKUHIBU_READ_FILE_NAME["normal_1"]
    )
    print(SetStockLendingRuisekiDay_gyaku_df)
    # ---累積---
    SetStockLendingRuisekiDay_ruiseki_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_004_RUIKEI_READ_FILE_NAME["normal_1"]
    )
    print(SetStockLendingRuisekiDay_ruiseki_df)
    # ---正解---
    SetStockLendingRuisekiDay_succes_1_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_004_CORRECT_ANSWER_FILE_NAME["normal_1"]
    )

    # --テスト実施--
    ruiseki_pd = gt.SetStockLendingRuisekiDay(
        SetStockLendingRuisekiDay_ruiseki_df,
        SetStockLendingRuisekiDay_gyaku_df
    )

    # 処理結果出力CSVファイル出力
    # --逆日歩不一致日付出力--
    ruiseki_pd.to_csv(
            Test_const.TEST_FILE_PATH
            + Test_const.TEST_003_RESULT_FILE_NAME["normal_1"]
    )

    print("\n★★★★ normal 1★★★★")
    print("\n--normal 1 input 1---")
    print(SetStockLendingRuisekiDay_gyaku_df)
    print("\n--normal 1 input 2---")
    print(SetStockLendingRuisekiDay_ruiseki_df)
    print("\n--normal 1 CORRECT_ANSWER---")
    print(SetStockLendingRuisekiDay_succes_1_df)
    print("\n--normal 1 RESULT_FILE---")
    print(ruiseki_pd)

    # --テスト確認--
    pd.testing.assert_frame_equal(
        left=ruiseki_pd,
        right=SetStockLendingRuisekiDay_succes_1_df)
