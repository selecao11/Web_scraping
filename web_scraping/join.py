# import re
import pandas as pd


class Join:

    hizuke_koumoku ='日付'
    join_kabuka_df = None
    join_shinyou_zan_df = None
    join_gyakuhibu_taisyaku_df = None

    def nikei_join_init(self, kabuka_df, shinyou_zan_df,
                        gyakuhibu_taisyaku_df):
        self.join_kabuka_df = kabuka_df
        self.join_shinyou_zan_df = shinyou_zan_df
        self.join_gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df

    def nikei_item_drop(self, kabu_shinyou_gyakuhibu_taisyaku_df):
        return kabu_shinyou_gyakuhibu_taisyaku_df

    # 日経各ワークフレームの結合
    def nikei_jion(self):
        tmp_df = pd.merge(self.join_kabuka_df, self.join_shinyou_zan_df,
                          how="outer", on=self.hizuke_koumoku)
        kabu_shinyou_gyakuhibu_taisyaku_df = pd.merge(
            tmp_df, self.join_gyakuhibu_taisyaku_df,
            how="outer", on=self.hizuke_koumoku)
        kabu_shinyou_gyakuhibu_taisyaku_df =\
            kabu_shinyou_gyakuhibu_taisyaku_df.fillna(0)
        kabu_shinyou_gyakuhibu_taisyaku_df =\
            self.nikei_item_drop(kabu_shinyou_gyakuhibu_taisyaku_df)
        print(kabu_shinyou_gyakuhibu_taisyaku_df)
        return kabu_shinyou_gyakuhibu_taisyaku_df
