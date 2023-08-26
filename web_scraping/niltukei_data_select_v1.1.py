# requests及びbs4を必ずインポートする
import requests
from bs4 import BeautifulSoup
import pandas as pd
import stock_related_select


from selenium import webdriver
import chrome_driver

#処理の開始を表示
class niltukei_data_select:

    def header_print():
        print("日経start")

    def title_start(title):
        print(title+" start")

    def title_end(title):
        print(title+" end")



    def data_get(chrome_driver):

        srs = stock_related_select()

        #差分の確認方法
        #https://qiita.com/higakin/items/59b60ed10ea0c0348362
        #取得
        syutoku_csv_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/取得株値整形済み/'+title+'_株価_信用残_逆日歩_貸借桟.csv')
        #累積
        ruiseki_csv_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/累積株値data/'+title+'_累積.csv')
        #差分を累積に追加
        #ruiseki_csv_df = pd.concat([ruiseki_csv_df, merge_df], axis=0)
        #print(ruiseki_csv_df)
        #マージデータフレームの不要項目削除
        drop_col = ['Unnamed: 0_x','Unnamed: 0_y']
        merge_df = merge_df.drop(drop_col, axis=1)

        #merge_df['累積逆日歩'] = merge_df['累積逆日歩'].str.replace('-', '0')

        sabun_df=merge_df[merge_df['_merge'] == "left_only"]

        sabun_drop_col = ['累積始値','累積高値','累積安値','累積終値','累積売買高','累積修正後終値' \
                        ,'累積信用売残','累積信用買残','累積信用倍率','累積逆日歩','累積日歩日数','累積貸株残','累積融資残']
        sabun_df = sabun_df.drop(sabun_drop_col, axis=1)

        sabun_df = sabun_df.rename(columns={'日付':'日付',\
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
        sabun_df["日付"] = pd.to_datetime(sabun_df["日付"])
        ruiseki_csv_df["日付"] = pd.to_datetime(ruiseki_csv_df["日付"])
        ruiseki_csv_df.to_csv('./ruiseki_TEST.csv')
        ruiseki_csv_df = ruiseki_csv_df.drop('Unnamed: 0', axis=1)
        ruiseki_csv_df = pd.concat([ruiseki_csv_df, sabun_df], axis=0)
        ruiseki_csv_df=ruiseki_csv_df.sort_values('日付',ascending=False)
        ruiseki_csv_df = ruiseki_csv_df.reset_index()
        ruiseki_csv_df = ruiseki_csv_df.drop('index', axis=1)
        ruiseki_csv_df = ruiseki_csv_df.drop('_merge', axis=1)
        ruiseki_csv_df.to_csv('./累積株値data/'+title+'_累積.csv')

        #差分データを追加した累積ファイルを記録
        ruiseki_csv_df.to_csv('./Cumulative_stock_price_data/'+title+'_累積.csv')
        #マージファイルのデータ差分を記録
        merge_df.to_csv('./Acquired_stock_price_adjusted/'+title+'_差分.csv')
        #マージファイルを記録
        merge_df.to_csv('./Cumulative_stock_price_data/'+title+'_マージ済み.csv')
        print("日経end")


chrome_driver = chrome_driver.chrome_driver_set()

nds =  niltukei_data_select()
for cmp in company:
    nds.title_start(title)
    nds.title_end(title)

nds.data_get(chrome_driver)
