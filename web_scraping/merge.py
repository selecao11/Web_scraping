import pandas as pd

class Merge:

    merge_ruiseki_df = None
    merge_nikei_data_df = None
    merge_df = None

    def nikei_merge_init(self,ruiseki_df,nikei_data_df):
        self.merge_ruiseki_df = ruiseki_df
        self.merge_nikei_data_df = nikei_data_df

    def nikei_merge(self):
        ruiseki_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/source/test/三菱自動車_累積.csv')
        nikei_data_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/source/test/三菱自動車_株価_信用残_逆日歩_貸借桟.csv')
        merge_df = pd.merge(ruiseki_df,nikei_data_df, on=["日付"],how='outer',indicator=True)
