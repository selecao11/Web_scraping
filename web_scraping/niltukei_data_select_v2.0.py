from niltuke_web import Niltukei_web
from niltukei_html import Niltukei_html
from niltukei_const import Niltukei_const
from kabuka_control import Kabuka_control
from gyakuhibu_control import Gyakuhibu_control
from shinyou_zan_control import Shinyou_zan_control
from join import Join
from merge import Merge
from stock_price_accumulation import StockPriceAccumulation
from ruiseki_control import Ruseki_control
from niltukei_company import Niltukei_company
from difference_control import Difference_control
import config


# 処理の開始を表示
class Niltukei_data_select:

    def header_print(self):
        import time
        import datetime
        print("日経start")
        print(datetime.datetime.fromtimestamp(time.time()))

    def tail_print(self):
        import time
        import datetime
        print("日経end")
        print(datetime.datetime.fromtimestamp(time.time()))

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
        """ Kabuka_controlインスタンスへ会社コードを渡す

        Args:
            company_code (string): 日経ページの企業コード

        Returns:
            DataFrame: 株価取得データフレーム
        """
        kc = Kabuka_control()
        return kc.cleateKabukadf(company_code)

    def niltukei_gyakuhibu_taisyaku(self, company_code):
        """ Gyakuhibu_controlインスタンスへ会社コードを渡す
        Args:
            company_code (string): 日経ページの企業コード

        Returns:
            DataFrame: 逆日歩取得データフレーム
        """
        gc = Gyakuhibu_control()
        return gc.cleateGyakuhibuTaisyakuDf(company_code)

    def niltukei_shinyou_zan(self, company_code):
        """Shinyou_zan_controlインスタンスへ会社コードを渡す

        Args:
            company_code (string): 日経ページの企業コード

        Returns:
            DataFrame: 信用残取得データフレーム
        """
        sz = Shinyou_zan_control()
        return sz.cleateShinyouZanDf(company_code)

    def niltukei_join(self, niltukei_data):
        """ 株価、逆日歩、信用フレームワークをそれぞれ結合する

        Args:
            niltukei_data (List): 株価、逆日歩、信用残格納List

        Returns:
            DataFrame: 株価、逆日歩、信用結合フレームワーク
        """
        jb = Join()
        return jb.jionNikei(niltukei_data)

    def createRuiseki(self):
        """ Ruiseki_controlインスタンスの生成

        Returns:
            Ruseki: Rusekiインスタンス
        """
        rc = Ruseki_control()
        return rc.readRuiseki()

    def niltukei_merge(self, niltukei_join_df):
        """ 株価、信用残、逆日歩の結合フレームワークと
            累積フレームワークの比較

        Args:
            niltukei_join_df (DataFrame): 株価、信用残、逆日歩の結合フレームワーク

        Returns:
            List: 結合フレームワークと累積フレームワークの比較結果
        """
        mg = Merge()
        # sz = Shinyou_zan()
        # driver = sz.getShinyouZanHtml(company_code,
        #                               sz.newShinyouZanDriver())
        ruikei_df = self.createRuiseki()
        return {"ruikei_df": ruikei_df,
                "nikei_merge": mg.mergeNikei(ruikei_df,
                                             niltukei_join_df)}

    def niltukei_difference(self, nikei_merge):
        """ Differenceインスタンスの生成と結合と累積フレームワークの差分の抽出

        Args:
            nikei_merge (_type_): 株価、信用残、逆日歩の結合フレームワーク

        Returns:
            DataFrame: 結合と累積フレームワークの差分のフレームワーク
        """
        dc = Difference_control()
        return dc.selectDifference(nikei_merge)

    def niltukei_stock_price_accumulation(self, ruiseki_df, difference_df):
        """ StockPriceAccumulationインスタンスの生成と差分の累積フレームワークへの追記

        Args:
            ruiseki_df (DataFrame): 累積フレームワーク
            difference_df (DataFrame): 差分フレームワーク
        """
        spa = StockPriceAccumulation()
        spa.accumulationStockPrice(
                                   ruiseki_df,
                                   difference_df)

    def getNiltukeiTitle(self, company_code):
        """日経ページからタイトル取得する。

        Args:
            company_code (string): 日経ページの企業コード
        """
        self.getNltukeiTitle(
            self.getNltukeiHtml(company_code,
                                self.newNiltukeiDriver())
        )
        import time
        import datetime
        print("【" + company_code + "】" + config.title + "start")
        print(datetime.datetime.fromtimestamp(time.time()))

    def title_end(title):
        print(title+" end")

    def niltukei_ruiseki_shift_create(self):
        import pandas as pd
        for name in Niltukei_const.FILE_NAME:
            ruiseki_df = pd.read_csv(Niltukei_const.CSV_PATH + name + ".csv")
            ruiseki_df_shift = ruiseki_df.shift(-1)
            # 終値差分算出
            ruiseki_df["終値差分"] = ruiseki_df_shift["累積終値"]\
                - ruiseki_df["累積終値"]

            ruiseki_df["UP"] = 0
            ruiseki_df["UP"][ruiseki_df["終値差分"] > 0] = 1
            # 終値前日比
            ruiseki_df["終値前日比"] = (ruiseki_df_shift["累積終値"]\
                - ruiseki_df["累積終値"]) / ruiseki_df_shift["累積終値"]

            # 終値前日比
            ruiseki_df["始値終値差分"] = ruiseki_df["累積始値"] - ruiseki_df["累積終値"]

            #隔週ごとの日数を入力
            list_week = []
            list_week = ruiseki_df['週'].unique()
            ruiseki_df['週日数']=0
            for i in list_week:
                ruiseki_df['週日数'][ruiseki_df['週'] == i ] = len(ruiseki_df[ruiseki_df['週']==i])


            ruiseki_df.to_csv(Niltukei_const.CSV_PATH + name
                              + '_MASTER'
                              + '.csv')

            #月曜日から金曜日まで５日分のデータのある週だけデータを取り出す
            ruiseki_sosoku_df=ruiseki_df[ruiseki_df['週日数'] ==5]
            ruiseki_sosoku_df=ruiseki_sosoku_df[ruiseki_sosoku_df['曜日'] !=4]
            ruiseki_sosoku_df.to_csv(Niltukei_const.CSV_PATH + name
                              + '_予測用'
                              + '.csv')

    def niltukei_ruiseki_create(self):
        niltukei_data = {}
        for company_code in Niltukei_const.COMPANYS:
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
            # 結合と累積との比較と差分の判断
            niltukei_merge_df =\
                self.niltukei_merge(niltukei_join_df,)
            # 結合と累積との差分抽出
            difference_df = self.niltukei_difference(
                niltukei_merge_df["nikei_merge"])
            # 差分を累積に追加
            self.niltukei_stock_price_accumulation(
                niltukei_merge_df["ruikei_df"], difference_df)

    def niltukei_main(self):
        self.header_print()
        # driver = self.get_driver()
        self.niltukei_ruiseki_create()
        self.niltukei_ruiseki_shift_create()
        self.tail_print()


nds = Niltukei_data_select()
nds.niltukei_main()
