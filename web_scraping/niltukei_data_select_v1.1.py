# requests及びbs4を必ずインポートする
# from bs4 import BeautifulSoup
import pandas as pd
# import stock_related_select

from kabuka_control import Kabuka_control
from gyakuhibu_control import Gyakuhibu_control
from shinyou_zan_control import Shinyou_zan_control
from join import Join
from merge import Merge
from stock_price_accumulation import StockPriceAccumulation
from difference import Difference
from niltukei_html import Niltukei_html
from niltukei_const import Niltukei_const
from ruiseki_control import Ruseki_control
from difference_control import Difference_control
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# import chrome_driver


# 処理の開始を表示
class Niltukei_data_select:

    # csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/tests/"
    csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"\
        "web_scraping/Cumulative_stock_price_data/"
    driver = None
    title = None
    shinyou_zan_df = None
    gyakuhibu_taisyaku_df = None
    kabu_df = None
    nikei_join_df = None
    merge_df = None
    difference_df = None
    ruiseki_df = None

    def header_print(self):
        print("日経start")

    def tail_print(self):
        print("日経end")

    def title_start(self, title):
        print(title+" start")

    def get_driver(self):
        driver_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"\
         "web_scraping/"
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        executable_path = driver_path + 'chromedriver_116'
        driver = webdriver.Chrome(executable_path, options=options)
        driver.maximize_window()
        return driver

    def company_html_get(self, cmp, driver):
        target_url = 'https://www.nikkei.com/nkd/company/?scode=' + cmp
        # driver = self.get_driver(target_url)
        driver.get(target_url)
        return driver

    def niltukei_kabu(self, driver):
        kc = Kabuka_control()
        niltukei_kabu = {}
        Kabuka_dict = {'WebDriverWait': WebDriverWait,
                       'driver': driver,
                       'pd': pd,
                       'By': By,
                       'csv_path': self.csv_path,
                       'title': kc.get_kabuka_html_title(driver)
                       }
        niltukei_kabu["kabu_df"] = kc.cleate_kabuka_df(Kabuka_dict)
        niltukei_kabu["title"] = kc.get_kabuka_html_title(driver)
        return niltukei_kabu

    def niltukei_gyakuhibu_taisyaku(self, driver):
        gc = Gyakuhibu_control()
        Gyakuhibu_dict = {'WebDriverWait': WebDriverWait,
                          'driver': driver,
                          'pd': pd,
                          'By': By,
                          'csv_path': self.csv_path,
                          'title': gc.get_gyakuhibu_html_title(driver)
                          }
        gyakuhibu_taisyaku_df = gc.cleate_gyakuhibu_taisyaku_df(Gyakuhibu_dict)
        return gyakuhibu_taisyaku_df

    def niltukei_shinyou_zan(self, driver):
        Shinyou_dict = {'WebDriverWait': WebDriverWait,
                        'driver': driver,
                        'pd': pd,
                        'By': By,
                        'csv_path': self.csv_path
                        }
        sz = Shinyou_zan_control()
        shinyou_zan_df = sz.cleate_shinyou_zan_df(Shinyou_dict)
        return shinyou_zan_df

    def niltukei_join(self, niltukei_data):
        jb = Join()

        """
        jb.nikei_join_init(niltukei_data["kabu"], niltukei_data["gyakuhibu"],
                           niltukei_data["shinyou_zan"])
        """
        return jb.nikei_jion(niltukei_data)

    def read_ruiseki(self, driver):
        rc = Ruseki_control()
        return rc.readRuiseki(self.csv_path, driver)

    def niltukei_merge(self, niltukei_join, driver):
        nh = Niltukei_html()
        mg = Merge()
        file_name = Niltukei_const.FILE_NAME_MEARGE
        mg.nikei_merge_init(self.read_ruiseki(driver), niltukei_join,
                            self.csv_path,
                            file_name, nh.get_html_title(driver))
        self.merge_df = mg.nikei_merge()

    def niltukei_difference(self):
        dc = Difference_control()
        dc.select_difference()
        df = Difference()
        file_name = Niltukei_const.FILE_NAME_DIFFERENCE
        #df.difference_init(self.merge_df, file_name, self.csv_path, self.title)
        self.difference_df = df.difference_select()

    def niltukei_stock_price_accumulation(self):
        # self.difference_df = pd.read_csv( self.csv_path +'_差分.csv')
        file_name = '_累積.csv'
        spa = StockPriceAccumulation()
        spa.stock_price_accumulation_init(self.difference_df, self.ruiseki_df,
                                          file_name, self.csv_path, self.title)
        spa.stock_price_accumulation()

    def title_end(title):
        print(title+" end")

    def niltukei_main(self):
        company = ['5631']
        '''
        company = [
            '5631', '7211', '3231', '7601', '6850', '7552', '3269', '6752',
            '7182', '8411', '3877', '7270', '9021', '7816', '7203', '5201',
            '9997', '9404', '6800', '4204', '6506', '7261']
        '''

        self.header_print()
        driver = self.get_driver()
        niltukei_data = {}
        for cmp in company:
            driver = self.company_html_get(cmp, driver)
            niltukei_data["kabu"] = self.niltukei_kabu(driver)
            niltukei_data["gyakuhibu"] =\
                self.niltukei_gyakuhibu_taisyaku(driver)
            niltukei_data["shinyou_zan"] = self.niltukei_shinyou_zan(driver)
            niltukei_join = self.niltukei_join(niltukei_data)
            self.niltukei_merge(niltukei_join, driver)
            self.niltukei_difference()
            self.niltukei_stock_price_accumulation()

        self.tail_print()


nds = Niltukei_data_select()
nds.niltukei_main()
