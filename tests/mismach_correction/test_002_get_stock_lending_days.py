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
    data_frame_df = Test_pres.readDataFrame(test_file_path, test_file_name)
    return data_frame_df


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
    # --入力ファイル--
    # ---累積---
    GetStockLendingDays_ruiseki_succes1_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_002_RUIKEI_READ_FILE_NAME["normal_1"]
    )
    # ---正解---
    GetStockLendingDays_succes_1_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_002_CORRECT_ANSWER_FILE_NAME["normal_1"]
    )

    # --テスト実施--
    ruiseki_disagreement_days_pd = gt.getStocklendingDays(
        GetStockLendingDays_ruiseki_succes1_df)

    # 処理結果出力CSVファイル出力
    # --取得日付出力--
    ruiseki_disagreement_days_pd.to_csv(
            Test_const.TEST_FILE_PATH
            + Test_const.TEST_002_RESULT_FILE_NAME["normal_1"]
    )

    print("\n--normal 1---")
    print("\n--normal 1 input---")
    print(GetStockLendingDays_ruiseki_succes1_df)
    print("\n--normal 1 CORRECT_ANSWER---")
    print(GetStockLendingDays_succes_1_df)
    print("\n--normal 1 RESULT_FILE---")
    print(ruiseki_disagreement_days_pd)

    # --テスト確認--
    #assert (ruiseki_disagreement_days_pd == GetStockLendingDays_succes_1_df)
    pd.testing.assert_frame_equal(
        left=ruiseki_disagreement_days_pd,
        right=GetStockLendingDays_succes_1_df)


def test_GetStockLendingDays_succes2():
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
    # --入力ファイル--
    # ---累積---
    GetStockLendingDays_ruiseki_succes2_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_002_RUIKEI_READ_FILE_NAME["normal_2"]
    )
    # ---正解---
    GetStockLendingDays_succes_2_df = readDataFrame(
            Test_const.TEST_FILE_PATH,
            Test_const.TEST_002_CORRECT_ANSWER_FILE_NAME["normal_2"]
    )

    # --テスト実施--
    ruiseki_disagreement_days_pd = gt.getStocklendingDays(
        GetStockLendingDays_ruiseki_succes2_df)

    # 処理結果出力CSVファイル出力
    # --取得日付出力--
    ruiseki_disagreement_days_pd.to_csv(
            Test_const.TEST_FILE_PATH
            + Test_const.TEST_002_RESULT_FILE_NAME["normal_2"]
    )

    print("\n--normal 2---")
    print("\n--normal 2 input---")
    print(GetStockLendingDays_ruiseki_succes2_df)
    print("\n--normal 2 CORRECT_ANSWER---")
    print(GetStockLendingDays_succes_2_df)
    print("\n--normal 2 RESULT_FILE---")
    print(ruiseki_disagreement_days_pd)

    #assert (ruiseki_disagreement_days_pd == GetStockLendingDays_succes_2_df)
    pd.testing.assert_frame_equal(left=ruiseki_disagreement_days_pd,
                                  right=GetStockLendingDays_succes_2_df)
