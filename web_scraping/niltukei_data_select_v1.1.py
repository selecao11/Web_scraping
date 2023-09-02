# requests及びbs4を必ずインポートする
from bs4 import BeautifulSoup
import pandas as pd
#import stock_related_select

from kabuka import Kabuka
from gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from shinyou_zan import Shinyou_zan
from join import Join
from merge import Merge
from stock_price_accumulation import StockPriceAccumulation
from selenium.webdriver.common.by import Bys
from difference import Difference
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
#import chrome_driver

#処理の開始を表示
class Niltukei_data_select:

    csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/tests/"
    driver = None
    title = None
    shinyou_zan_df = None
    gyakuhibu_taisyaku_df = None
    kabu_df = None
    nikei_join_df = None
    merge_df = None
    difference_df = None
    ruiseki_df = None


    def header_print():
        print("日経start")

    def tail_print():
        print("日経end")

    def title_start(title):
        print(title+" start")

    def driver_get(self):
        driver_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/tests"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        executable_path = driver_path + 'chromedriver_116'
        self.driver = webdriver.Chrome(executable_path, options=options)

    def company_html_get(self,cmp):
        self.driver.maximize_window()
        target_url = 'https://www.nikkei.com/nkd/company/?scode='+ cmp
        self.driver.get(target_url)


    def niltukei_kabu(self):
        kb = Kabuka()
        file_name = '_test_株価.csv'
        kb.kabuka_title_get(self.driver)
        kb.kabuka_taisyaku_init_set(file_name,self.csv_path)
        self.title = kb.kabuka_title_get(self.driver)
        self.kabu_df = kb.kabuka_df_cleate(WebDriverWait,self.driver,pd,Bys,self.csv_path,file_name)

    def niltukei_gyakuhibu_taisyaku(self):
        gt = Gyakuhibu_taisyaku()
        file_name = '_test_逆日歩_貸借桟.csv'
        gt.gyakuhibu_taisyaku_title_get(self.driver)
        gt.gyakuhibu_taisyaku_init_set(file_name,self.csv_path)
        self.gyakuhibu_taisyaku_df = gt.gyakuhibu_taisyaku_df_cleate(WebDriverWait,self.driver,pd,Bys)

    def niltukei_shinyou_zan(self):
        sz = Shinyou_zan()
        file_name = '_test_信用残.csv'
        sz.shinyou_zan_title_get(self.driver)
        sz.shinyou_zan_init_set(file_name,self.driver)
        self.shinyou_zan_df = sz.shinyou_zan_df_cleate(WebDriverWait,self.driver,pd,Bys)

    def niltukei_join(self):
        jb = Join()
        jb.nikei_join_init(self.kabu_df,self.gyakuhibu_taisyaku_df,self.shinyou_zan_df)
        self.nikei_join_df = jb.nikei_jion()

    def niltukei_merge(self):
        self.ruiseki_df = pd.read_csv(self.csv_path + self.title +'_累積.csv')
        mg = Merge()
        file_name = '_マージ.csv'
        mg.nikei_merge_init(self.ruiseki_df,self.nikei_join_df,self.csv_path,file_name,self.title)
        self.merge_df = mg.nikei_merge()

    def niltukei_difference(self):
        df = Difference()
        file_name = '_差分.csv'
        df.difference_init(self.merge_df,file_name,self.csv_path,self.title)
        self.difference_df = df.difference_select()

    def niltukei_stock_price_accumulation(self):
        self.difference_df = pd.read_csv( +'_差分.csv')
        file_name = '_累積.csv'
        spa = StockPriceAccumulation()
        spa.stock_price_accumulation_init(self.difference_df,self.ruiseki_df,file_name,self.csv_path,self.title)
        spa.stock_price_accumulation()

    def title_end(title):
        print(title+" end")

    def niltukei_main(self):
        company = ['7211','3231','7601','6850','7552','3269','6752','7182','8411','3877','7270','9021','7816','7203','5201','9997',
        '9404','6800','4204','6506','7261']

        #srs = stock_related_select()
        self.header_print()
        self.driver_get()
        for cmp in company:
            self.company_html_get(cmp)
            self.niltukei_kabu()
            self.niltukei_gyakuhibu_taisyaku()
            self.niltukei_shinyou_zan()
            self.niltukei_join()
            self.niltukei_merge()
            self.niltukei_difference()
            self.niltukei_stock_price_accumulation()

        self.tail_print()

nds= Niltukei_data_select()
nds.niltukei_main()
