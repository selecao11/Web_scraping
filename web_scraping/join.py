# import re
import pandas as pd
from niltukei_const import Niltukei_const


class Join:

    def dropNikeiitem(self, kabu_shinyou_gyakuhibu_taisyaku_df):
        return kabu_shinyou_gyakuhibu_taisyaku_df

    def jionNikei(self, niltukei_data):
        # kabu = niltukei_data["kabu"]
        """ 株価、逆日歩、信用フレームワークを結合する
        Args:
            niltukei_data (List): 株価、逆日歩、信用残格納List
        Returns:
            niltukei_join_df(DataFrame): 株価、逆日歩、信用残結合データフレーム
        """
        # 株価データフレームと信用残データフレームを結合する
        tmp_df = pd.merge(niltukei_data["kabu"], niltukei_data["shinyou_zan"],
                          how="outer", on=Niltukei_const.HIZEKE_KOUMOKU)
        # 逆日歩データフレームを結合する
        niltukei_join_df = pd.merge(
            tmp_df, niltukei_data["gyakuhibu"],
            how="outer", on=Niltukei_const.HIZEKE_KOUMOKU)
        # データフレームのNonを全て0にする
        niltukei_join_df =\
            niltukei_join_df.fillna(0)
        # niltukei_join_df =\
        #    self.dropNikeiitem(niltukei_join_df)
        return niltukei_join_df
