import re
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from niltuke_web import Niltukei_web
from niltukei_company import Niltukei_company

class Shinyou_zan:

    hizuke_koumoku = '日付'
    shinyou_uri_kaisetu_koumoku = '信用売残 （解説）'
    shinyou_uri_koumoku = '信用売残'
    shinyou_kai_kaisetu_koumoku = '信用買残 （解説）'
    shinyou_kai_koumoku = '信用買残'
    shinyou_bai_kaisetu_koumoku = '信用倍率 （解説）'
    shinyou_bai_koumoku = '信用倍率'
    shinyou_zan_search = "信用残"
    kabuka_search = '株価'

    shinyou_zan_path = None
    shinyou_zan_file_name = None
    shinyou_zan_sz_title = None
    shinyou_zan_df = None

    def cleateShinyouZanDf(self, kabuka_html):
        return pd.read_html(kabuka_html)

    def newShinyouZanDriver(self):
        nw = Niltukei_web()
        return nw.cleate_driver()

    def shinyou_zan_init_set(self, file_name, path):
        self.shinyou_zan_path = path
        self.shinyou_zan_file_name = file_name

    def getShinyouZanHtml(self, company_code, driver):
        nc = Niltukei_company()
        return nc.getCompanyHtml(company_code, driver)


    # 信用桟のhtml取得
    def shinyou_zan_html_search(self, driver):
        kabuka = WebDriverWait(driver, 10).until(lambda x: x.find_element(
            By.LINK_TEXT, self.kabuka_search))
        kabuka.click()
        shinyou_zan = WebDriverWait(driver, 10).until(lambda x: x.find_element(
            By.LINK_TEXT, self.shinyou_zan_search))
        shinyou_zan.click()
        shinyou_zan_table = WebDriverWait(driver, 10).until(
            lambda y: y.find_element(By.CLASS_NAME, "w668"))
        # table要素を含むhtmlを取得
        shinyou_zan_html = shinyou_zan_table.get_attribute("outerHTML")
        return shinyou_zan_html

    # 企業名取得
    def shinyou_zan_title_get(self, driver):
        self.shinyou_zan_sz_title = re.search(r'【(.+)】', driver.title).group(1)

    # 信用桟データフレームカラム変更
    def shinyou_zan_df_rename(self, shinyou_df):
        shinyou_df = shinyou_df.rename(columns={
            self.hizuke_koumoku: self.hizuke_koumoku,
            self.shinyou_uri_kaisetu_koumoku: self.shinyou_uri_koumoku,
            self.shinyou_kai_kaisetu_koumoku: self.shinyou_kai_koumoku,
            self.shinyou_bai_kaisetu_koumoku: self.shinyou_bai_koumoku})
        return shinyou_df

