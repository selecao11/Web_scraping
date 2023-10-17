# import re
import pandas as pd
from niltukei_const import Niltukei_const


class Join:

    hizuke_koumoku = '日付'
    join_kabuka_df = None
    join_shinyou_zan_df = None
    join_gyakuhibu_taisyaku_df = None

    """
    def nikei_join_init(self, kabuka_df, shinyou_zan_df,
                        gyakuhibu_taisyaku_df):
        self.join_kabuka_df = kabuka_df
        self.join_shinyou_zan_df = shinyou_zan_df
        self.join_gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df
    """
    def dropNikeiitem(self, kabu_shinyou_gyakuhibu_taisyaku_df):
        return kabu_shinyou_gyakuhibu_taisyaku_df

    # 日経各ワークフレームの結合
    def jionNikei(self, niltukei_data):
        # kabu = niltukei_data["kabu"]
        tmp_df = pd.merge(niltukei_data["kabu"], niltukei_data["shinyou_zan"],
                          how="outer", on=Niltukei_const.HIZEKE_KOUMOKU)
        niltukei_join_df = pd.merge(
            tmp_df, niltukei_data["gyakuhibu"],
            how="outer", on=Niltukei_const.HIZEKE_KOUMOKU)
        niltukei_join_df =\
            niltukei_join_df.fillna(0)
        niltukei_join_df =\
            self.dropNikeiitem(niltukei_join_df)
        return niltukei_join_df
