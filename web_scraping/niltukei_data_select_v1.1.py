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
        kabuka_dict = {'WebDriverWait': WebDriverWait,
                       'driver': driver,
                       'pd': pd,
                       'By': By,
                       'csv_path': self.csv_path,
                       'title': kc.getKabukaHtmlTitle(driver)
                       }
        niltukei_kabu["kabu_df"] = kc.cleateKabukadf(kabuka_dict, driver)
        return niltukei_kabu

    def niltukei_gyakuhibu_taisyaku(self, driver):
        gc = Gyakuhibu_control()
        gyakuhibu_dict = {'WebDriverWait': WebDriverWait,
                          'driver': driver,
                          'pd': pd,
                          'By': By,
                          'csv_path': self.csv_path,
                          'title': gc.getGyakuhibuHtmlTitle(driver)
                          }
        gyakuhibu_taisyaku_df = gc.cleateGyakuhibuTaisyakuDf(gyakuhibu_dict,
                                                             driver)
        return gyakuhibu_taisyaku_df

    def niltukei_shinyou_zan(self, driver):
        shinyou_dict = {'WebDriverWait': WebDriverWait,
                        'driver': driver,
                        'pd': pd,
                        'By': By,
                        'csv_path': self.csv_path
                        }
        sz = Shinyou_zan_control()
        shinyou_zan_df = sz.cleateShinyouZanDf(shinyou_dict)
        return shinyou_zan_df

    def niltukei_join(self, niltukei_data):
        jb = Join()
        return jb.jionNikei(niltukei_data)

    def readRuiseki(self, driver):
        rc = Ruseki_control()
        return rc.readRuiseki(self.csv_path, driver)

    def niltukei_merge(self, niltukei_join_df, driver):
        mg = Merge()
        ruikei_df = self.readRuiseki(driver)
        merge_dict = {
                        'csv_path': self.csv_path,
                        'driver': driver
                        }
        return {"ruikei_df": ruikei_df,
                "nikei_merge": mg.mergeNikei(merge_dict, ruikei_df,
                                             niltukei_join_df)}

    def niltukei_difference(self, niltukei_join, driver):
        dc = Difference_control()
        difference_dict = {
                'csv_path': self.csv_path
                }
        return dc.selectDifference(difference_dict, niltukei_join, driver)

    def niltukei_stock_price_accumulation(self, ruiseki_df, difference_df,
                                          driver):
        # self.difference_df = pd.read_csv( self.csv_path +'_差分.csv')
        stock_price_dict = {
                'csv_path': self.csv_path,
                'driver': driver
                }
        spa = StockPriceAccumulation()
        spa.accumulationStockPrice(stock_price_dict,
                                   ruiseki_df,
                                   difference_df)

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
            niltukei_join_df = self.niltukei_join(niltukei_data)
            niltukei_merge_df = self.niltukei_merge(niltukei_join_df, driver)
            aaa = niltukei_merge_df["nikei_merge"]
            ruikei_df = niltukei_merge_df["ruikei_df"]
            difference_df = self.niltukei_difference(aaa, driver)
            self.niltukei_stock_price_accumulation(ruikei_df,
                                                   difference_df,
                                                   driver)

        self.tail_print()


nds = Niltukei_data_select()
nds.niltukei_main()
