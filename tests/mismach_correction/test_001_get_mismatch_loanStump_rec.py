import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import pandas as pd
from tests.test_pure import Test_pres

from web_scraping.ruseki_mismatch import RuisekiMismatch
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
    rm = RuisekiMismatch()
    return rm


def readDataFrame(test_file_path, test_file_name):
    data_df = Test_pres.readDataFrame(test_file_path, test_file_name)
    return data_df


def test_mismatch_loanstump_rec_normal_1():
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
    # --入力ファイル--
    # ---逆日歩---
    mismatch_loanstump_rec_gyaku_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_GYAKUHIBU_READ_FILE_NAME["normal_1"]
    )
    # ---累積---
    mismatch_loanstump_rec_ruiseki_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_RUIKEI_READ_FILE_NAME["normal_1"]
    )
    # ---正解---
    mismatch_loanstump_rec_normal_1_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_CORRECT_ANSWER_FILE_NAME["normal_1"]
    )
    # --テスト実施--
    result_df = rm.getMismatchLoanStumpRec(
        mismatch_loanstump_rec_ruiseki_df,
        mismatch_loanstump_rec_gyaku_df
    )
    # 処理結果出力CSVファイル出力
    # --不一致レコードの出力--
    result_df.to_csv(
        Test_const.TEST_FILE_PATH
        + Test_const.TEST_001_RESULT_FILE_NAME["normal_1"]
    )

    print("\n★★★★ normal 2★★★★")
    print("\n--normal 1 input gyaku_df---")
    print(mismatch_loanstump_rec_gyaku_df)
    print("\n--normal 1 input ruiseki_df---")
    print(mismatch_loanstump_rec_ruiseki_df)
    print("\n--normal 1 CORRECT_ANSWER---")
    print(mismatch_loanstump_rec_normal_1_df)
    print("\n--normal 1 RESULT_FILE---")
    print(result_df)
    pd.testing.assert_frame_equal(
        left=result_df,
        right=mismatch_loanstump_rec_normal_1_df
    )


def test_mismatch_loanstump_rec_normal_2():
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
    # --入力ファイル--
    # ---逆日歩---
    mismatch_loanstump_rec_gyaku_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_GYAKUHIBU_READ_FILE_NAME["normal_1"]
    )
    # ---累積---
    mismatch_loanstump_rec_ruiseki_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_RUIKEI_READ_FILE_NAME["normal_2"]
    )
    mismatch_loanstump_rec_normal_2_df = readDataFrame(
        Test_const.TEST_FILE_PATH,
        Test_const.TEST_001_CORRECT_ANSWER_FILE_NAME["normal_2"]
    )
    # --テスト実施--
    result_df = rm.getMismatchLoanStumpRec(
        mismatch_loanstump_rec_ruiseki_df,
        mismatch_loanstump_rec_gyaku_df
    )

    # 処理結果出力CSVファイル出力
    # --不一致レコードの出力--
    result_df.to_csv(
        Test_const.TEST_FILE_PATH
        + Test_const.TEST_001_RESULT_FILE_NAME["normal_2"]
    )

    print("\n★★★★ normal 2★★★★")
    print("\n--normal 2 input gyaku_df---")
    print(mismatch_loanstump_rec_gyaku_df)
    print("\n--normal 2 input ruiseki_df---")
    print(mismatch_loanstump_rec_ruiseki_df)
    print("\n--normal 2 CORRECT_ANSWER---")
    print(mismatch_loanstump_rec_normal_2_df)
    print("\n--normal 2 RESULT_FILE---")
    print(result_df)

    pd.testing.assert_frame_equal(
        left=result_df,
        right=mismatch_loanstump_rec_normal_2_df
    )
