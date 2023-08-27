import pandas as pd
import re


class Difference:

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

    merge_df = None
    difference_df = None

    def difference_init(self,merge_df):
        self.merge_df = merge_df

    def colum_drop(self):
        #self.difference_df = self.difference_df.drop("Unnamed: 0", axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_UNNAMED_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_HAJIMARINE_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_TAKENE_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_YASUNE_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_OWARINE_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_URIKAIDAKA_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SYUSEIGO_OWARINE_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SHINYOU_URI_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SHINYOU_KAI_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SHINYOU_BAI_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_GYAKUHIBU_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_HIBU_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_KASHIKABU_ZAN, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_YUSHI_ZAN_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU, axis=1)

    def colum_rename(self):
        self.difference_df = self.difference_df.rename(columns={'日付':'日付',\
                                            '始値':'累積始値',\
                                            '高値':'累積高値',\
                                            '安値':'累積安値',\
                                            '終値':'累積終値',\
                                            '売買高':'累積売買高',\
                                            '修正後終値':'累積修正後終値',\
                                            '信用売残':'累積信用売残',\
                                            '信用買残':'累積信用買残',\
                                            '信用倍率':'累積信用倍率',\
                                            '逆日歩':'累積逆日歩',\
                                            '日歩日数':'累積日歩日数',\
                                            '貸株残':'累積貸株残',\
                                            '融資残':'累積融資残',})


    def difference_select(self):
        self.difference_df = self.merge_df[self.merge_df["_merge"] == "left_only"]
        print(self.difference_df)
        #self.colum_rename()
        self.colum_drop()
        return self.difference_df
