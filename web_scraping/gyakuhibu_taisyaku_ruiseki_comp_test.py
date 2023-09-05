import pandas as pd
def gyakuhibu_taisyaku_zan_ruiseki_comp():
        csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"

        gyakuhibu_taisyaku_df = pd.read_csv(csv_path +'スノーピーク_test_逆日歩_貸借桟.csv')
        ruiseki_df = pd.read_csv(csv_path + 'スノーピーク_累積.csv')
        ruiseki_df["日付"]=ruiseki_df["日付"].astype("datetime64[ns]")
        #逆日歩_貸株残と累積でデータ誤差の有無のチェック
        ruiseki_Non_stock_lending_df = ruiseki_df[~ruiseki_df['累積貸株残'].isin(gyakuhibu_taisyaku_df['貸株残'])]
        #累積のデータ誤差発生日を抽出
        diff_days=list()
        for day in ruiseki_Non_stock_lending_df["日付"]:
                diff_days.append(day.strftime('%Y-%m-%d'))         
        #逆日歩_貸借桟の該当日データを抽出
        gyakuhibu_day_df = gyakuhibu_taisyaku_df[gyakuhibu_taisyaku_df['日付'].isin(diff_days)]
        #逆日歩_貸借桟の貸株残を累積に出力
        i_list=list()
        for d in diff_days:
                i_list.append(ruiseki_df.index[ruiseki_df['日付']==d])
        stock_load_balance = gyakuhibu_day_df.loc[:,'貸株残'].values
        for i,v in enumerate(i_list):
                print(i)
                ruiseki_df.loc[v,'累積貸株残']=stock_load_balance[i]
        ruiseki_df.to_csv(csv_path + 'shinyou_zan_df_comp.csv')

gyakuhibu_taisyaku_zan_ruiseki_comp()
