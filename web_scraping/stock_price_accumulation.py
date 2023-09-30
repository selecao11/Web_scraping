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

    def colum_drop(self, ruiseki_df):
        return ruiseki_df.drop(Niltukei_const.UNNAMED_0_KOUMOKU, axis=1)

        '''self.accumulation_df = self.accumulation_df.drop\
            ('index', axis=1) '''
    def stock_price_accumulation_sort(self, ruiseki_df):
        return ruiseki_df.sort_values('日付', ascending=False)

    def stock_price_accumulation_reset_index(self, ruiseki_df):
        return ruiseki_df.reset_index(drop=True)

    def stock_price_accumulation(self,
                                 stock_price_dict,
                                 ruiseki_df,
                                 difference_df,
                                 driver):
        nh = Niltukei_html()
        ruiseki_df = pd.concat([ruiseki_df, difference_df], axis=0)
        ruiseki_df = self.colum_drop(
            self.stock_price_accumulation_reset_index(
                self.stock_price_accumulation_sort(ruiseki_df))
        )
        ruiseki_df.to_csv(stock_price_dict["csv_path"]
                                    + nh.getHtmlTitle(driver)
                                    + self.stock_price_accumulation_file_name)
