# from hizuke import Hizuke
from shinyou_zan import Shinyou_zan
from niltukei_const import Niltukei_const
from ruiseki_control import Ruseki_control
import pandas as pd
from niltukei_html import Niltukei_html


class Shinyou_zan_control:

    def updataRuikei(self, company_code,
                     shinyou_zan_driver,
                     shinyou_zan_df):
        # 逆日歩貸借データフレームを参考に累積の累積貸株残で不一致の項目を更新する
        rc = Ruseki_control()
        sz = Shinyou_zan()
        ruiseki_df = rc.readRuiseki()
        missmatch_koumoku = ["信用売残", "信用買残", "信用倍率"]
        data_frame = shinyou_zan_df
        for missmatch in missmatch_koumoku:
            ruiseki_df = rc.updataMismatchRuikei(company_code,
                                                 shinyou_zan_driver,
                                                 missmatch,
                                                 ruiseki_df,
                                                 data_frame)

    def cleateShinyouZanDf(self, company_code):
        sz = Shinyou_zan()
        shinyou_zan_driver = sz.getShinyouZanHtml(company_code,
                                               sz.newShinyouZanDriver())
        shinyou_zan_html = sz.shinyou_zan_html_search(
            shinyou_zan_driver)
        # tableをDataFrameに格納
        shinyou_zan_df = sz.cleateShinyouZanDf(shinyou_zan_html)
        shinyou_zan_df = shinyou_zan_df[0]
        # 信用桟データフレームのカラム名の変更
        shinyou_zan_df = sz.shinyou_zan_df_rename(shinyou_zan_df)
        shinyou_zan_df[Niltukei_const.HIZEKE_KOUMOKU] = pd.to_datetime(
            shinyou_zan_df[Niltukei_const.HIZEKE_KOUMOKU])
        # 逆日歩貸借データフレームを参考に累積の累積貸株残で不一致の項目を更新する
        self.updataRuikei(company_code,
                          shinyou_zan_driver,
                          shinyou_zan_df)
        # 取得したデータを記録
        nh = Niltukei_html()
        shinyou_zan_df.to_csv(Niltukei_const.CSV_PATH
                                     + nh.getHtmlTitle(shinyou_zan_driver)
                                     + Niltukei_const.FILE_NAME_SHINYOU)
        return shinyou_zan_df
