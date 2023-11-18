# from hizuke import Hizuke
from shinyou_zan import Shinyou_zan
from niltukei_const import Niltukei_const
from ruiseki_control import Ruseki_control
import pandas as pd
# from niltukei_html import Niltukei_html
from ruseki_mismatch import RuisekiMismatch
import config


class Shinyou_zan_control:

    def updataRuikei(self, company_code,
                     shinyou_zan_driver,
                     shinyou_zan_df):
        """ 信用残データフレームを参考に累積の累積貸株残で不一致の項目を更新する
        Args:
            company_code (string): 日経ページの企業コード
            shinyou_zan_driver (driver): 信用残のドライバー
            shinyou_zan_df (DataFrame): 信用残データフレーム
        """
        rc = Ruseki_control()
        rm = RuisekiMismatch()
        ruiseki_df = rc.readRuiseki()

        missmatch_koumoku = [Niltukei_const.SHINYOU_URI_KOUMOKU,
                             Niltukei_const.SHINYOU_KAI_KOUMOKU,
                             Niltukei_const.SHINYOU_BAI_KOUMOKU]
        # missmatch_koumoku = ["信用売残", "信用買残", "信用倍率"]
        data_frame = shinyou_zan_df
        for missmatch in missmatch_koumoku:
            ruiseki_df = rc.updataMismatchRuikei(company_code,
                                                 shinyou_zan_driver,
                                                 missmatch,
                                                 ruiseki_df,
                                                 data_frame)
        rm.saveMismatchRuseki(rm.dropRuseki(ruiseki_df))

    def cleateShinyouZanDf(self, company_code):
        """ 信用残データフレームを生成する
        Args:
            company_code (string): 日経ページの企業コード

        Returns:
            shinyou_zan_df(DataFrame): 信用残データフレーム
        """
        sz = Shinyou_zan()
        shinyou_zan_driver = sz.getShinyouZanHtml(company_code,
                                                  sz.newShinyouZanDriver())
        shinyou_zan_html = sz.shinyou_zan_html_search(
            shinyou_zan_driver)
        # 使用済のドライバの開放
        sz.delShinyouDriver(shinyou_zan_driver)
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
        # nh = Niltukei_html()
        shinyou_zan_df.to_csv(Niltukei_const.CSV_PATH
                              + config.title
                              + Niltukei_const.FILE_NAME_SHINYOU)
        return shinyou_zan_df
