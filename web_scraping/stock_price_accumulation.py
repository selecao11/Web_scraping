from  web_scraping.hizuke import Hizuke
import pandas as pd
import re


class StockPriceAccumulation:

    difference_df = None
    stock_price_accumulation_df = None

    def stock_price_accumulation_init(self,difference_df,stock_price_accumulation_df):
        self.difference_df = difference_df #差分
        self.stock_price_accumulation_df = stock_price_accumulation_df #累積

    def stock_price_accumulation(self):
        accumulation_df = pd.concat([self.stock_price_accumulation_df, self.difference_df], axis=0)
        #accumulation_df = pd.merge(self.difference_df,self.stock_price_accumulation_df, on=["日付"],how='outer',indicator=True)
        return accumulation_df
