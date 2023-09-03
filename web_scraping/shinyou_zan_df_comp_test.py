    def shinyou_zan_df_comp(self):
        self.ruiseki_df = pd.read_csv(self.shinyou_zan_path + self.shinyou_zan_sz_title +'_累積.csv')
        self.ruiseki_df["日付"]=self.ruiseki_df["日付"].astype("datetime64[ns]")
        shinyou_zan_merge_df = pd.merge(self.ruiseki_df,self.shinyou_zan_df, on=["日付",],how='outer',indicator=True)
        shinyou_zan_df = shinyou_zan_merge_df[shinyou_zan_merge_df["_merge"] == "both"]
        shinyou_zan_df=(shinyou_zan_df["累積信用売残"]==shinyou_zan_df["信用売残"])
        file_name="_both.csv"
        print('--累積信用売残==信用売残 start--')
        print(shinyou_zan_df)
        print('--累積信用売残==信用売残 end--')
        shinyou_zan_df.to_csv(self.shinyou_zan_path + self.shinyou_zan_sz_title + file_name)
        pass
