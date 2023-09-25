# requests及びbs4を必ずインポートする
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import pandas as pd

import data_select as ds

# HTMLの取得先として当サイトを指定する
#response = requests.get("https://pig-data.jp")

# BeautifulSoup4でサイトのテキストを取得し、
# 第二因数にhtml.parserを指定、解析結果をsoupに入れる

# soup.find_all('a', text=True))でaタグに指定されている要素を抽出、
# print(element.getText())でテキストのみを出力する
#from bs4 import BeautifulSoup
from selenium import webdriver
import re

print("日経start")

options = webdriver.ChromeOptions()
options.add_argument('--headless')
#executable_path = '/home/user/anaconda3/envs/web_scraping/source/chromedriver_116'
executable_path = '/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/chromedriver_116'
driver = webdriver.Chrome(executable_path, options=options)

#driver = webdriver.Chrome('./chromedriver')
driver.maximize_window()

company = ['5631','7211','3231','7601','6850','7552','3269','6752','7182','8411','3877','7270','9021','7816','7203','5201','9997',
'9404','6800','4204','6506','7261']
#company = ['7211']
csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/"

for c in company:
    target_url = 'https://www.nikkei.com/nkd/company/?scode='+ c
    soup = BeautifulSoup(target_url,'html.parser')
    driver.get(target_url)

    title = re.search(r'【(.+)】',driver.title).group(1)
    print(title+" start")

    # 株価取得
    kabu_df =  ds.call_kabuka(title,WebDriverWait,driver,pd,By)
    # 信用残取得
    shinyou_df =  ds.call_shinyou_zan(title,WebDriverWait,driver,pd,By)
    kabu_shinyou_data_df = pd.merge(kabu_df, shinyou_df, how="outer", on="日付")

    # 逆日残_貸借表取得
    gyakuhibu_taisyaku_df = ds.call_gyakuhibu_taisyaku(title,WebDriverWait,driver,pd,By)
    #データフレームから逆日歩の列を削除
    gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.drop('日証金', axis=1)
    #株価、信用残、逆日残を日付を基準にマージ
    kabu_shinyou_gyakuhibu_taisyaku_data_df = pd.merge(kabu_shinyou_data_df, gyakuhibu_taisyaku_df, how="outer", on="日付")
    kabu_shinyou_gyakuhibu_taisyaku_data_df=kabu_shinyou_gyakuhibu_taisyaku_data_df.fillna(0)
    print(kabu_shinyou_gyakuhibu_taisyaku_data_df)
    #取得株値整形済みファイルを記録
    kabu_shinyou_gyakuhibu_taisyaku_data_df.to_csv(csv_path +'Acquired_stock_price_adjusted/'+title+'_株価_信用残_逆日歩_貸借桟.csv')
    pass
    print(title+" end")
    #取得株値整形済みファイルを取得
    syutoku_csv_df = pd.read_csv(csv_path + 'Acquired_stock_price_adjusted/'+title+'_株価_信用残_逆日歩_貸借桟.csv')
    #累積
    ruiseki_csv_df = pd.read_csv(csv_path + 'Cumulative_stock_price_data/Accumulation_old/'+title+'_累積.csv')
    merge_df = pd.merge(syutoku_csv_df,ruiseki_csv_df, on=["日付"],how='outer',indicator=True)

#    print(merge_df)

    merge_df["日付"] = pd.to_datetime(merge_df["日付"])
    merge_df=merge_df.sort_values('日付',ascending=False)
    #print(merge_df[日付].fillna(0))
    #merge_df.to_csv('/home/user/anaconda3/envs/web_scraping/source/'+title+'_merge.csv')
    #merge_df =merge_df.fillna({"日付":0})

    #差分を抽出
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
    #ruiseki_csv_df = ruiseki_csv_df.drop('Unnamed: 0', axis=1)
    ruiseki_csv_df = pd.concat([ruiseki_csv_df, sabun_df], axis=0)
    ruiseki_csv_df=ruiseki_csv_df.sort_values('日付',ascending=False)
    ruiseki_csv_df = ruiseki_csv_df.reset_index()
    ruiseki_csv_df = ruiseki_csv_df.drop('index', axis=1)
    ruiseki_csv_df = ruiseki_csv_df.drop('_merge', axis=1)

    #差分データを追加した累積ファイルを記録
    ruiseki_csv_df.to_csv(csv_path + 'Cumulative_stock_price_data/'+title+'_累積.csv')
    #マージファイルのデータ差分を記録
    merge_df.to_csv('test_マージ.csv')
    merge_df.to_csv(csv_path + 'Acquired_stock_price_adjusted/'+title+'_差分.csv')
    #マージファイルを記録
    merge_df.to_csv(csv_path + 'Cumulative_stock_price_data/'+title+'_マージ済み.csv')
    print("日経end")
