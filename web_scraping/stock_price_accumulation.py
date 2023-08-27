import pandas as pd


class StockPriceAccumulation:

    STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU = 'Unnamed: 0'

    difference_df = None
    stock_price_accumulation_df = None
    accumulation_df = None

    def stock_price_accumulation_init(self,difference_df,stock_price_accumulation_df):
        self.difference_df = difference_df #差分
        self.stock_price_accumulation_df = stock_price_accumulation_df #累積

    def colum_drop(self):
        self.accumulation_df = self.accumulation_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU, axis=1)

    def stock_price_accumulation(self):
        self.accumulation_df = pd.concat([self.stock_price_accumulation_df, self.difference_df], axis=0)
        #print(accumulation_df)
        self.colum_drop()
        return self.accumulation_df
