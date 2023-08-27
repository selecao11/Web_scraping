import pandas as pd
import re


class StockPriceAccumulation:


    STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU='Unnamed: 0'
    STOCK_PRICE_ACCUMULATION_HAJIMARINE_KOUMOKU='始値'
    STOCK_PRICE_ACCUMULATION_TAKENE_KOUMOKU='高値'
    STOCK_PRICE_ACCUMULATION_YASUNE_KOUMOKU='安値'
    STOCK_PRICE_ACCUMULATION_OWARINE_KOUMOKU='終値'
    STOCK_PRICE_ACCUMULATION_URIKAIDAKA_KOUMOKU='売買高'
    STOCK_PRICE_ACCUMULATION_SYUSEIGO_OWARINE_KOUMOKU='修正後終値'
    STOCK_PRICE_ACCUMULATION_SHINYOU_URI_KOUMOKU =  '信用売残'
    STOCK_PRICE_ACCUMULATION_SHINYOU_KAI_KOUMOKU =  '信用買残'
    STOCK_PRICE_ACCUMULATION_SHINYOU_BAI_KOUMOKU =  '信用倍率'
    STOCK_PRICE_ACCUMULATION_GYAKUHIBU_KOUMOKU = '逆日歩'
    STOCK_PRICE_ACCUMULATION_HIBU_KOUMOKU = '日歩日数'
    STOCK_PRICE_ACCUMULATION_KASHIKABU_ZAN = '貸株残'
    STOCK_PRICE_ACCUMULATION_YUSHI_ZAN_KOUMOKU = '融資残'
    STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU = '_merge' 
    difference_df = None
    stock_price_accumulation_df = None


    def stock_price_accumulation_init(self,difference_df,stock_price_accumulation_df):
        self.difference_df = difference_df #差分
        self.stock_price_accumulation_df = stock_price_accumulation_df #累積

    def colum_drop(self):
        self.stock_price_accumulation_df = self.stock_price_accumulation_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU, axis=1)
        
        self.stock_price_accumulation_df = self.stock_price_accumulation_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_HAJIMARINE_KOUMOKU, axis=1)

        self.stock_price_accumulation_df = self.stock_price_accumulation_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_TAKENE_KOUMOKU, axis=1)

        self.stock_price_accumulation_df = self.stock_price_accumulation_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_TAKENE_KOUMOKU, axis=1)



    STOCK_PRICE_ACCUMULATION_YASUNE_KOUMOKU='安値'
    STOCK_PRICE_ACCUMULATION_OWARINE_KOUMOKU='終値'
    STOCK_PRICE_ACCUMULATION_URIKAIDAKA_KOUMOKU='売買高'
    STOCK_PRICE_ACCUMULATION_SYUSEIGO_OWARINE_KOUMOKU='修正後終値'
    STOCK_PRICE_ACCUMULATION_SHINYOU_URI_KOUMOKU =  '信用売残'
    STOCK_PRICE_ACCUMULATION_SHINYOU_KAI_KOUMOKU =  '信用買残'
    STOCK_PRICE_ACCUMULATION_SHINYOU_BAI_KOUMOKU =  '信用倍率'
    STOCK_PRICE_ACCUMULATION_GYAKUHIBU_KOUMOKU = '逆日歩'
    STOCK_PRICE_ACCUMULATION_HIBU_KOUMOKU = '日歩日数'
    STOCK_PRICE_ACCUMULATION_KASHIKABU_ZAN = '貸株残'
    STOCK_PRICE_ACCUMULATION_YUSHI_ZAN_KOUMOKU = '融資残'
    STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU = '_merge' 



    def stock_price_accumulation(self):
        accumulation_df = pd.concat([self.stock_price_accumulation_df, self.difference_df], axis=0)
        self.colum_drop()
        return accumulation_df
