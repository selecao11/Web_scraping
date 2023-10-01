import pandas as pd
from niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html


class StockPriceAccumulation:

    STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU = 'Unnamed: 0'

    # 差分データフレーム
    difference_df = None
    # 累積データフレーム
    stock_price_accumulation_df = None
    # 新累積データフレーム
    accumulation_df = None
    stock_price_accumulation_path = None
    stock_price_accumulation_file_name = None
    stock_price_accumulation_title = None

    def stock_price_accumulation_init(
            self, difference_df, stock_price_accumulation_df,
            file_name, file_path, title):
        self.difference_df = difference_df  # 差分
        self.stock_price_accumulation_df = stock_price_accumulation_df  # 累積
        self.stock_price_accumulation_path = file_path
        self.stock_price_accumulation_file_name = file_name
        self.stock_price_accumulation_title = title

    def dropColum(self, ruiseki_df):
        return ruiseki_df.drop(Niltukei_const.UNNAMED_0_KOUMOKU, axis=1)

    def sortStockPriceDate(self, ruiseki_df):
        return ruiseki_df.sort_values(Niltukei_const.HIZEKE_KOUMOKU,
                                      ascending=False)

    def resetStockPriceIndex(self, ruiseki_df):
        return ruiseki_df.reset_index(drop=True)

    def accumulationStockPrice(self,
                               stock_price_dict,
                               ruiseki_df,
                               difference_df):
        nh = Niltukei_html()
        ruiseki_df = pd.concat([ruiseki_df, difference_df], axis=0)
        ruiseki_df = self.dropColum(
            self.resetStockPriceIndex(
                self.sortStockPriceDate(ruiseki_df))
        )
        ruiseki_df.to_csv(stock_price_dict["csv_path"]
                          + nh.getHtmlTitle(stock_price_dict["driver"])
                          + Niltukei_const.FILE_NAME_RUISEKI)
