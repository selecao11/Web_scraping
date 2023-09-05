import pandas as pd

csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"
gyakuhibu_taisyaku_df = None
ruiseki_df = None
ruiseki_Non_stock_lending_df = None
gyakuhibu_day_df = None
stock_load_balance = None

def gyakuhibu_taisyaku_zan_loan_balance_comp():
        pass

def gyakuhibu_taisyaku_zan_comp_init():
        gyakuhibu_taisyaku_df = pd.read_csv(csv_path +'スノーピーク_test_逆日歩_貸株残.csv')
        ruiseki_df = pd.read_csv(csv_path + 'スノーピーク_累積.csv')

def gyakuhibu_taisyaku_zan_stock_lending_not_isin():
        ruiseki_Non_stock_lending_df = ruiseki_df[~ruiseki_df['累積貸株残'].isin(gyakuhibu_taisyaku_df['貸株残'])]

def gyakuhibu_taisyaku_zan_stock_lending_isin(diff_days):
        gyakuhibu_day_df = gyakuhibu_taisyaku_df[gyakuhibu_taisyaku_df['日付'].isin(diff_days)]

def gyakuhibu_taisyaku_zan_stock_lending_append():
        diff_days=list()
        for day in ruiseki_Non_stock_lending_df["日付"]:
                diff_days.append(day.strftime('%Y-%m-%d'))         
        return diff_days

def gyakuhibu_taisyaku_zan_stock_lending_extra(diff_days):
        i_list=list()
        for d in diff_days:
                i_list.append(ruiseki_df.index[ruiseki_df['日付']==d])
        stock_load_balance = gyakuhibu_day_df.loc[:,'貸株残'].values
        return i_list

def gyakuhibu_taisyaku_zan_stock_output(i_list):
        for i,v in enumerate(i_list):
                print(i)
                ruiseki_df.loc[v,'累積貸株残']=stock_load_balance[i]
        return ruiseki_df

def gyakuhibu_taisyaku_zan_stock_lending_comp():
        ruiseki_df["日付"]=ruiseki_df["日付"].astype("datetime64[ns]")
        #逆日歩_貸株残と累積でデータ誤差の有無のチェック
        gyakuhibu_taisyaku_zan_stock_lending_not_isin()
        #累積のデータ誤差発生日を抽出
        diff_days = gyakuhibu_taisyaku_zan_stock_lending_append
        #逆日歩_貸借s桟の該当日データを抽出
        gyakuhibu_taisyaku_zan_stock_lending_isin(diff_days)
        #逆日歩_貸借桟の貸株残を累積に出力
        i_list = gyakuhibu_taisyaku_zan_stock_lending_extra(diff_days)
        ruiseki_df = gyakuhibu_taisyaku_zan_stock_output(i_list)
        ruiseki_df.to_csv(csv_path + 'shinyou_zan_df_comp.csv')

gyakuhibu_taisyaku_zan_stock_lending_comp
