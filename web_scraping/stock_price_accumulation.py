import pandas as pd
from  web_scraping.niltukei_const import Niltukei_const

class StockPriceAccumulation:

    STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU = 'Unnamed: 0'

    #差分データフレーム
    difference_df = None
    #累積データフレーム
    stock_price_accumulation_df = None
    #新累積データフレーム
    accumulation_df = None
    stock_price_accumulation_path  = None
    stock_price_accumulation_file_name  = None
    stock_price_accumulation_title  = None

    def stock_price_accumulation_init(self,difference_df,stock_price_accumulation_df,file_name,file_path,title):
        self.difference_df = difference_df #差分
        self.stock_price_accumulation_df = stock_price_accumulation_df #累積
        self.stock_price_accumulation_path = file_path
        self.stock_price_accumulation_file_name = file_name
        self.stock_price_accumulation_title = title

    def colum_drop(self):
        self.accumulation_df = self.accumulation_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_UNNAMED_0_KOUMOKU, axis=1)
        '''self.accumulation_df = self.accumulation_df.drop\
            ('index', axis=1) '''
    def stock_price_accumulation_sort(self):
        self.accumulation_df=self.accumulation_df.sort_values('日付',ascending=False)

    def stock_price_accumulation_reset_index(self):
        self.accumulation_df = self.accumulation_df.reset_index(drop=True)

    def stock_price_accumulation(self):
        self.accumulation_df = pd.concat([self.stock_price_accumulation_df, self.difference_df], axis=0)
        #print(accumulation_df)
        self.stock_price_accumulation_sort()
        self.stock_price_accumulation_reset_index()
        self.colum_drop()
        self.accumulation_df.to_csv(self.stock_price_accumulation_path + \
                                    self.stock_price_accumulation_title + \
                                    self.stock_price_accumulation_file_name)
        return self.accumulation_df
