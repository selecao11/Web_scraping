import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.hizuke import Hizuke
from niltukei_html import Niltukei_html
from niltuke_web import Niltukei_web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from niltukei_const import Niltukei_const
import pandas as pd
import re
from niltukei_company import Niltukei_company 

class Gyakuhibu_taisyaku:

    hizuke_koumoku = '日付'
    gyakuhibu_taisyaku_Unnamed1_koumoku = 'Unnamed: 1'
    gyakuhibu_taisyaku_nicyoukin_koumoku = '日証金'
    gyakuhibu_taisyaku_en_gyakuhibu_koumoku = '逆日歩（円）'
    gyakuhibu_taisyaku_gyakuhibu_koumoku = '逆日歩'
    gyakuhibu_taisyaku_hi_hibu_koumoku = '日歩日数（日）'
    gyakuhibu_taisyaku_hibu_koumoku = '日歩日数'
    gyakuhibu_taisyaku_kabu_kashikabu_koumoku_zan = '貸株残（株）'
    gyakuhibu_taisyaku_kashikabu_koumoku_zan = '貸株残'
    gyakuhibu_taisyaku_kabu_yushi_koumoku_zan = '融資残（株）'
    gyakuhibu_taisyaku_yushi_koumoku_zan = '融資残'

    gyakuhibu_taisyaku_search = "逆日歩・貸借残"
    kabuka_search = '株価'

    gyakuhibu_taisyaku_path = None
    gyakuhibu_taisyaku_file_name = None
    gyakuhibu_taisyaku_title = None

    def cleateGyakuhibuDf(self, kabuka_html):
        return pd.read_html(kabuka_html)

    # 株価取得ドライバの生成
    def newGyakuhibuDriver(self):
        nw = Niltukei_web()
        return nw.cleateDriver()

    def getGyakuhibuHtml(self, company_code, driver):
        nc = Niltukei_company()
        return nc.getCompanyHtml(company_code, driver)

    def gyakuhibu_taisyaku_hizuke_yy_add(self, gyakuhibu_taisyaku_df, hizuke,
                                         hizuke_df):
        # 逆日歩貸借データフレームの月日に年を追加
        hizuke_df = hizuke.year_add(hizuke_df)
        gyakuhibu_taisyaku_df[self.hizuke_koumoku] = hizuke_df
        gyakuhibu_taisyaku_df[self.hizuke_koumoku] = pd.to_datetime(
            gyakuhibu_taisyaku_df[self.hizuke_koumoku])
        return gyakuhibu_taisyaku_df

    def gyakuhibu_taisyaku_youbi_del(self, kabu_df, hizuke, hizuke_df):
        # 逆日歩貸借データフレームの曜日文字を削除
        hizuke_df = kabu_df[self.hizuke_koumoku]
        hizuke_df = hizuke.day_of_week_delete(hizuke_df)
        return hizuke_df

    # ここから
    def gyakuhibu_taisyaku_init_set(self, file_name, file_path):
        self.gyakuhibu_taisyaku_path = file_path
        self.gyakuhibu_taisyaku_file_name = file_name

    # データフレームから逆日歩、日歩日数の列を置換
    def gyakuhibu_taisyaku_item_replace(self, gyakuhibu_taisyaku_df):
        gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.replace(
            {'逆日歩': {'-': 0}})
        gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.replace(
            {'日歩日数': {'-': 0}})
        return gyakuhibu_taisyaku_df

    # データフレームから日証金の列を削除
    def gyakuhibu_taisyaku_item_drop(self, gyakuhibu_taisyaku_df):
        gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.drop('日証金', axis=1)
        return gyakuhibu_taisyaku_df

    # 逆日歩貸借のhtml取得
    def searchGyakuhibuHtml(self, driver):
        kabuka = WebDriverWait(driver, 10).until(lambda x: x.find_element(
            By.LINK_TEXT, Niltukei_const.HTML_KABUKA_SEARCH))
        kabuka.click()
        gyakuhibu_taisyaku = WebDriverWait(driver, 10).until(
            lambda x: x.find_element(By.LINK_TEXT,
                                     Niltukei_const.HTML_GYAKUBU_SEARCH
                                     ))
        gyakuhibu_taisyaku.click()
        gyakuhibu_taisyaku_table = WebDriverWait(driver, 10).until(
            lambda y: y.find_element(By.CLASS_NAME,
                                     Niltukei_const.HTML_W668_SEARCH))
        # table要素を含むhtmlを取得
        gyakuhibu_taisyaku_html = gyakuhibu_taisyaku_table.get_attribute(
            Niltukei_const.HTML_OUTER_HTML_SEARCH)
        return gyakuhibu_taisyaku_html

    """     # 企業名取得
    def gyakuhibu_taisyaku_title_get(self, driver):
        self.gyakuhibu_taisyaku_title = re.search(r'【(.+)】',
                                                  driver.title).group(1)
    """
    def getGyakuhibuTitle(self, driver):
        nh = Niltukei_html()
        return nh.getHtmlTitle(driver)
    # re.search(r'【(.+)】', driver.title).group(1)

    # 逆日歩貸借データフレームカラム変更
    def gyakuhibu_taisyaku_df_rename(self, gyakuhibu_taisyaku_df):
        gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.rename(
            columns={self.hizuke_koumoku: self.hizuke_koumoku,
                     self.gyakuhibu_taisyaku_Unnamed1_koumoku:
                     self.gyakuhibu_taisyaku_nicyoukin_koumoku,
                     self.gyakuhibu_taisyaku_en_gyakuhibu_koumoku:
                     self.gyakuhibu_taisyaku_gyakuhibu_koumoku,
                     self.gyakuhibu_taisyaku_hi_hibu_koumoku:
                     self.gyakuhibu_taisyaku_hibu_koumoku,
                     self.gyakuhibu_taisyaku_kabu_kashikabu_koumoku_zan:
                     self.gyakuhibu_taisyaku_kashikabu_koumoku_zan,
                     self.gyakuhibu_taisyaku_kabu_yushi_koumoku_zan:
                     self.gyakuhibu_taisyaku_yushi_koumoku_zan
                     })
        return gyakuhibu_taisyaku_df
