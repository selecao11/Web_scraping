import pandas as pd
from  web_scraping.niltukei_const import Niltukei_const

class Difference:

    merge_df = None
    difference_df = None

    difference_path = None
    difference_file_name = None
    difference_title = None

    def difference_init(self,merge_df,file_name,file_path,title):
        self.merge_df = merge_df
        self.difference_path = file_path
        self.difference_file_name = file_name
        self.difference_title = title

    def colum_drop(self):
        #Unnamed: 0
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_UNNAMED_0_KOUMOKU, axis=1)

        #累積始値
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_HAJIMARINE_KOUMOKU, axis=1)

        #累積高値
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_TAKENE_KOUMOKU, axis=1)

        #累積安値
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_YASUNE_KOUMOKU, axis=1)

        #累積終値
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_OWARINE_KOUMOKU, axis=1)

        #累積売買高
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_URIKAIDAKA_KOUMOKU, axis=1)

        #累積修正後終値
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SYUSEIGO_OWARINE_KOUMOKU, axis=1)

        #累積信用売残
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SHINYOU_URI_KOUMOKU, axis=1)

        #累積信用買残
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SHINYOU_KAI_KOUMOKU, axis=1)

        #累積信用倍率
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SHINYOU_BAI_KOUMOKU, axis=1)

        #累積逆日歩
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_GYAKUHIBU_KOUMOKU, axis=1)

        #累積日歩日数
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_HIBU_KOUMOKU, axis=1)

        #累積貸株残
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_KASHIKABU_ZAN, axis=1)

        #累積融資残
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_YUSHI_ZAN_KOUMOKU, axis=1)

        #_merge
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU, axis=1)

    '''
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_TAKENE_KOUMOKU, axis=1)

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_YASUNE_KOUMOKU, axis=1)
#累積売買高

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_OWARINE_KOUMOKU, axis=1)
#累積修正後終値

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_URIKAIDAKA_KOUMOKU, axis=1)
#累積信用売残

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SYUSEIGO_OWARINE_KOUMOKU, axis=1)
#累積信用買残

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SHINYOU_URI_KOUMOKU, axis=1)
#累積信用倍率

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SHINYOU_KAI_KOUMOKU, axis=1)
#累積逆日歩

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_SHINYOU_BAI_KOUMOKU, axis=1)
#累積日歩日数

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_GYAKUHIBU_KOUMOKU, axis=1)
#累積貸株残

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_HIBU_KOUMOKU, axis=1)
#累積融資残

        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_KASHIKABU_ZAN, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_YUSHI_ZAN_KOUMOKU, axis=1)
        self.difference_df = self.difference_df.drop\
            (self.STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU, axis=1)
    '''
    def colum_rename(self):
        """

            HIZEKE_KOUMOKU
    ='始値'
    ='高値'
    ='安値'
    ='終値'
    ='売買高'
    ='修正後終値'
     =  '信用売残'
     =  '信用買残'
     =  '信用倍率'
     = '逆日歩'
     = '日歩日数'
     = '貸株残'
     = '融資残'
    STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU = '_merge' 

                STOCK_PRICE_ACCUMULATION_UNNAMED_0_KOUMOKU='Unnamed: 0'
    ='累積始値'
    ='累積高値'
    ='累積安値'
    ='累積終値'
    ='累積売買高'
    ='累積修正後終値'
     =  '累積信用売残'
     =  '累積信用買残'
     =  '累積信用倍率'
     = '累積逆日歩'
     = '累積日歩日数'
     = '累積貸株残'
     = '累積融資残'
    STOCK_PRICE_ACCUMULATION_MERGE_KOUMOKU = '_merge' 

        """
        self.difference_df = self.difference_df.rename(columns=\
            {Niltukei_const.STOCK_PRICE_ACCUMULATION_HAJIMARINE_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_HAJIMARINE_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_TAKENE_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_TAKENE_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_YASUNE_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_YASUNE_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_OWARINE_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_OWARINE_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_URIKAIDAKA_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_URIKAIDAKA_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_SYUSEIGO_OWARINE_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SYUSEIGO_OWARINE_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_SHINYOU_URI_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SHINYOU_URI_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_SHINYOU_KAI_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SHINYOU_KAI_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_SHINYOU_BAI_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_SHINYOU_BAI_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_GYAKUHIBU_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_GYAKUHIBU_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_HIBU_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_HIBU_KOUMOKU,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_KASHIKABU_ZAN:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_KASHIKABU_ZAN,\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_YUSHI_ZAN_KOUMOKU:\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_RUISEKI_YUSHI_ZAN_KOUMOKU,})


    def difference_select(self):
        self.difference_df = self.merge_df[self.merge_df["_merge"] == "right_only"]
        print(self.difference_df)
        self.colum_drop()
        self.colum_rename()
        self.difference_df.to_csv(self.difference_path + self.difference_title + self.difference_file_name)
        return self.difference_df
