from ruiseki import Ruseki
from ruseki_mismatch import RuisekiMismatch
from niltukei_const import Niltukei_const


class Ruseki_control:

    def readRuiseki(self, csv_path, driver):
        ru = Ruseki()
        return ru.readRuseki(csv_path, driver)

    def updataStockLendingMismatch(self, ruiseki_df, gyaku_df):
        '''
            逆日歩の貸株残と累積の累積貸株残で不一致の行を抽出し、
            貸株残で累積貸株残を上書きする

                param
            ---------------
            ruiseki_df                  : data frame
                累積のデータフレーム
            gyaku_df                    : data frame
                逆日歩のデータフレーム

                return
            ---------------
            ruiseki_df                  :data frame
                変更後の累積のデータフレーム
        '''
        rm = RuisekiMismatch()
        ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU] = \
            self.ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU]\
                .astype(Niltukei_const.DATE_TIME64_NS)
        # 逆日歩_貸株残と累積でデータ誤差の有無のチェック
        ruiseki_mismatch_df = rm.getMismatchLoanStumpRec(
            ruiseki_df, gyaku_df)
        # 累積のデータ誤差発生日を抽出
        ruiseki_mismatch_days_df =\
            rm.getStockLendingMismatchDays(ruiseki_mismatch_df)
        # 逆日歩_貸株残の該当日データを抽出
        gyaku_mismatch_df =\
            rm.getGyakuStockLendingMismatchDays(ruiseki_mismatch_days_df,
                                                gyaku_df)
        # 逆日歩_貸借桟の貸株残を累積に出力
        updata_ruiseki_df = \
            self.updataRuisekiDay(ruiseki_df, gyaku_mismatch_df)
        """
        self.ruiseki_df = \
        self.SetRuisekiDfStockLoadBalance(gyaku_disagreement_days)
        """
        csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"\
            "web_scraping/Cumulative_stock_price_data/"

        updata_ruiseki_df.to_csv(csv_path + '累積_更新後.csv')
        ruiseki_df.to_csv(csv_path + '累積_更新前.csv')
