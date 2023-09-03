import pandas as pd
def shinyou_zan_df_comp():
        csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"

        gyakuhibu_taisyaku_df = pd.read_csv(csv_path +'スノーピーク_test_逆日歩_貸借桟.csv')
        ruiseki_df = pd.read_csv(csv_path + 'スノーピーク_累積.csv')
        ruiseki_df["日付"]=ruiseki_df["日付"].astype("datetime64[ns]")
        ruiseki_df = ruiseki_df[~ruiseki_df['累積貸株残'].isin(gyakuhibu_taisyaku_df['貸株残'])]
        dd = ruiseki_df["日付"][1].strftime('%Y-%m-%d')
        #iterrow()
        #dd = ruiseki_df.loc[1,"日付"].

        print(dd)

        #ruiseki_df.loc[ruiseki_df[["日付"] == gyakuhibu_taisyaku_df["日付"]],gyakuhibu_taisyaku_df['貸株残']]
        ruiseki_df.to_csv(csv_path + 'shinyou_zan_df_comp.csv')
        '''
        shinyou_zan_merge_df = pd.merge(self.ruiseki_df,self.shinyou_zan_df, on=["日付",],how='outer',indicator=True)
        shinyou_zan_df = shinyou_zan_merge_df[shinyou_zan_merge_df["_merge"] == "both"]
        shinyou_zan_df=(shinyou_zan_df["累積信用売残"]==shinyou_zan_df["信用売残"])
        file_name="_both.csv"
        print('--累積信用売残==信用売残 start--')
        print(shinyou_zan_df)
        print('--累積信用売残==信用売残 end--')
        shinyou_zan_df.to_csv(self.shinyou_zan_path + self.shinyou_zan_sz_title + file_name)
        '''
        pass

shinyou_zan_df_comp()
