# requests及びbs4を必ずインポートする
import pandas as pd

from niltuke_web import Niltukei_web
from niltukei_html import Niltukei_html
from kabuka_control import Kabuka_control
from gyakuhibu_control import Gyakuhibu_control
from shinyou_zan_control import Shinyou_zan_control
from join import Join
from merge import Merge
from stock_price_accumulation import StockPriceAccumulation
from niltukei_const import Niltukei_const
from ruiseki_control import Ruseki_control
from niltukei_company import Niltukei_company
from difference_control import Difference_control
from selenium.webdriver.common.by import By
from shinyou_zan import Shinyou_zan
import config


# 処理の開始を表示
class Niltukei_data_select:


    """     title = None
        shinyou_zan_df = None
        gyakuhibu_taisyaku_df = None
        kabu_df = None
        nikei_join_df = None
        merge_df = None
        difference_df = None
        ruiseki_df = None
    """
    def header_print(self):
        import time
        print("日経start")
        print(time.time())

    def tail_print(self):
        import time
        print("日経end")
        print(time.time())

    def title_start(self, title):
        print(title+" start")

    # タイトル取得
    def getNltukeiTitle(self, driver):
        nh = Niltukei_html()
        config.title = nh.getHtmlTitle(driver)

    # HTML取得
    def getNltukeiHtml(self, company_code, driver):
        nc = Niltukei_company()
        return nc.getCompanyHtml(company_code, driver)

    # ドライバー生成
    def newNiltukeiDriver(self):
        nw = Niltukei_web()
        return nw.cleateDriver()

    def niltukei_kabu(self, company_code):
        kc = Kabuka_control()
        niltukei_kabu = {}
        niltukei_kabu["kabu_df"] = kc.cleateKabukadf(company_code)
        return niltukei_kabu

    def niltukei_gyakuhibu_taisyaku(self, company_code):
        gc = Gyakuhibu_control()
        gyakuhibu_taisyaku_df = gc.cleateGyakuhibuTaisyakuDf(company_code)
        return gyakuhibu_taisyaku_df

    def niltukei_shinyou_zan(self, company_code):
        sz = Shinyou_zan_control()
        shinyou_zan_df = sz.cleateShinyouZanDf(company_code)
        return shinyou_zan_df

    def niltukei_join(self, niltukei_data):
        jb = Join()
        return jb.jionNikei(niltukei_data)

    def readRuiseki(self, driver):
        rc = Ruseki_control()
        return rc.readRuiseki()

    def niltukei_merge(self, company_code, niltukei_join_df):
        mg = Merge()
        sz = Shinyou_zan()
        driver = sz.getShinyouZanHtml(company_code,
                                      sz.newShinyouZanDriver())
        ruikei_df = self.readRuiseki(driver)
        return {"ruikei_df": ruikei_df,
                "nikei_merge": mg.mergeNikei(ruikei_df,
                                             niltukei_join_df)}

    def niltukei_difference(self, niltukei_join):
        dc = Difference_control()
        return dc.selectDifference(niltukei_join)

    def niltukei_stock_price_accumulation(self, ruiseki_df, difference_df):
        # self.difference_df = pd.read_csv( self.csv_path +'_差分.csv')
        spa = StockPriceAccumulation()
        spa.accumulationStockPrice(
                                   ruiseki_df,
                                   difference_df)

    def getNiltukeiTitle(self, company_code):
        config.titile = self.getNltukeiTitle(
            self.getNltukeiHtml(company_code,
                                self.newNiltukeiDriver())
        )

    def title_end(title):
        print(title+" end")

    def niltukei_main(self):
        companys = ['5631', '7211', '3231']
        """         companys = [
                    '5631', '7211', '3231', '7601', '6850', '7552', '3269', '6752',
                    '7182', '8411', '3877', '7270', '9021', '7816', '7203', '5201',
                    '9997', '9404', '6800', '4204', '6506', '7261']
        """
        self.header_print()
        # driver = self.get_driver()
        niltukei_data = {}
        for company_code in companys:
            # タイトル取得
            self.getNiltukeiTitle(company_code)
            # 株価取得
            niltukei_data["kabu"] = self.niltukei_kabu(company_code)
            # 逆日歩取得
            niltukei_data["gyakuhibu"] =\
                self.niltukei_gyakuhibu_taisyaku(company_code)
            # 信用残取得
            niltukei_data["shinyou_zan"] =\
                self.niltukei_shinyou_zan(company_code)
            # 株価、逆日歩、信用残結合
            niltukei_join_df = self.niltukei_join(niltukei_data)
            # 結合と累積との比較
            niltukei_merge_df =\
                self.niltukei_merge(company_code, niltukei_join_df,)
            aaa = niltukei_merge_df["nikei_merge"]
            ruikei_df = niltukei_merge_df["ruikei_df"]
            # 結合と累積との差分抽出
            difference_df = self.niltukei_difference(aaa)
            # 差分を累積に追加
            self.niltukei_stock_price_accumulation(ruikei_df,
                                                   difference_df)
        self.tail_print()


nds = Niltukei_data_select()
nds.niltukei_main()
