import pandas as pd
from niltukei_const import Niltukei_const
# from niltukei_html import Niltukei_html
from ruiseki import Ruseki
import config


class StockPriceAccumulation:

    STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU = 'Unnamed: 0'

    # 差分データフレーム
    # difference_df = None
    # 累積データフレーム
    # stock_price_accumulation_df = None
    # 新累積データフレーム
    # accumulation_df = None
    # stock_price_accumulation_path = None
    # stock_price_accumulation_file_name = None
    # stock_price_accumulation_title = None

    def dropColum(self, ruiseki_df):
        return ruiseki_df.drop(Niltukei_const.UNNAMED_0_KOUMOKU, axis=1)

    def sortStockPriceDate(self, ruiseki_df):
        return ruiseki_df.sort_values(Niltukei_const.HIZEKE_KOUMOKU,
                                      ascending=False)

    def resetStockPriceIndex(self, ruiseki_df):
        """ 累計データフレームのIndexを振り直す
        Args:
            ruiseki_df (DataFrame): 累計データフレーム
        Returns:
             ruiseki_df (DataFrame): 累計データフレーム
        """
        return ruiseki_df.reset_index(drop=True)

    def updateWeekDayRuiseki(self, ruiseki_df):
        """ 累計データフレームに週項目を追加して何周目か更新する
        Args:
            ruiseki_df (DataFrame): 累計データフレーム
        Returns:
             ruiseki_df (DataFrame): 累計データフレーム
        """
        from datetime import datetime
        from datetime import timedelta
        # 2023/1/1を1週目とする
        start = datetime(2023, 1, 1)
        # 何周目かを計算し更新する
        ruiseki_df["週"] = (ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU] - start) \
            // timedelta(weeks=1)
        return ruiseki_df

    def resetIndexRuiseki(self, ruiseki_df):
        """ 累計データフレームのColume順の変更とIndexを振り直す為、Rusekiを生成する
        Args:
            ruiseki_df (DataFrame): 累計データフレーム
        Returns:
            ruiseki_df (DataFrame): 累計データフレーム
        """
        rs = Ruseki()
        return rs.resetIndexRuseki(ruiseki_df)

    def accumulationStockPrice(self,
                               ruiseki_df,
                               difference_df):
        """ 累計データフレームに差分のデータフレームを追加する
        Args:
            ruiseki_df (DataFrame): 累計データフレーム
            difference_df (DataFrame): 差分データフレーム
        """
        # 差分を縦に追加する
        ruiseki_df = pd.concat([ruiseki_df, difference_df], axis=0)
        ruiseki_df = self.dropColum(
            self.resetStockPriceIndex(
                self.sortStockPriceDate(ruiseki_df))
        )
        # データが何週目を計算
        ruiseki_df = self.updateWeekDayRuiseki(ruiseki_df)
        # Colume順の変更とIndexの振り直し
        ruiseki_df = self.resetIndexRuiseki(ruiseki_df)
        ruiseki_df.to_csv(Niltukei_const.CSV_PATH
                          + config.title
                          + Niltukei_const.FILE_NAME_RUISEKI)
