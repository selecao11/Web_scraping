class merge:

            #データフレームから逆日歩の列を削除
    gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.drop('日証金', axis=1)
    #株価、信用残、逆日残を日付を基準にマージ
    def merge_make(kabu_shinyou_data_df,syutoku_csv_df,gyakuhibu_taisyaku_df,ruiseki_csv_df):
        kabu_shinyou_gyakuhibu_taisyaku_data_df = pd.merge(kabu_shinyou_data_df, gyakuhibu_taisyaku_df, how="outer", on="日付")
        kabu_shinyou_gyakuhibu_taisyaku_data_df=kabu_shinyou_gyakuhibu_taisyaku_data_df.fillna(0)
        print(kabu_shinyou_gyakuhibu_taisyaku_data_df)
        kabu_shinyou_gyakuhibu_taisyaku_data_df.to_csv('./取得株値整形済み/'+title+'_株価_信用残_逆日歩_貸借桟.csv')

        merge_df = pd.merge(syutoku_csv_df,ruiseki_csv_df, on=["日付"],how='outer',indicator=True)
        print(merge_df)

        merge_df["日付"] = pd.to_datetime(merge_df["日付"])
        merge_df=merge_df.sort_values('日付',ascending=False)
        merge_df =merge_df.fillna(0)
        return merge_df
