import pandas as pd
def shinyou_zan_df_comp():
        csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"

        gyakuhibu_taisyaku_df = pd.read_csv(csv_path +'スノーピーク_test_逆日歩_貸借桟.csv')
        ruiseki_df = pd.read_csv(csv_path + 'スノーピーク_累積.csv')
        ruiseki_df["日付"]=ruiseki_df["日付"].astype("datetime64[ns]")
        #逆日歩_貸株残と累積でデータ誤差の有無のチェック
        ruiseki_Non_stock_lending_df = ruiseki_df[~ruiseki_df['累積貸株残'].isin(gyakuhibu_taisyaku_df['貸株残'])]
        #累積のデータ誤差発生日を抽出
        bbb=list()
        bbb.append(ruiseki_Non_stock_lending_df.loc[1,"日付"].strftime('%Y-%m-%d'))
        print(bbb)
        #逆日歩_貸借桟の該当日データを抽出
        aaa = gyakuhibu_taisyaku_df[gyakuhibu_taisyaku_df['日付'].isin(bbb)]
        #逆日歩_貸借桟の貸株残を抽出
        ccc = aaa.loc[:,'貸株残'].values
        print(ccc)
        print(bbb[0])
        ruiseki_df.loc[ruiseki_df['日付']==bbb[0],'累積貸株残']=0
        #逆日歩_貸株残の日付で累積データを抽出

        ruiseki_df.to_csv(csv_path + 'shinyou_zan_df_comp.csv')

shinyou_zan_df_comp()
