from hizuke import Hizuke
import pandas as pd
import re
from niltukei_html import Niltukei_html
from niltuke_web import Niltukei_web
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from niltukei_const import Niltukei_const
from niltukei_company import Niltukei_company


class Kabuka:

    hizuke_koumoku = '日付'
    hajimarine_koumoku = '始値'
    takane_koumoku = '高値'
    yasune_koumoku = '安値'
    owarine_koumoku = '終値'
    urikaidaka_koumoku = '売買高'
    syuseigoatai_koumoku = '修正後終値'
    kabuka_koumoku = '株価'

    kabuka_title = None
    kabuka_taisyaku_path = None
    kabuka_taisyaku_file_name = None

    def kabuka_hizuke_yy_add(self, kabu_df, hizuke, hizuke_df):
        # 日付項目の月日に年を追加
        hizuke_df = hizuke.year_add(hizuke_df)
        kabu_df[self.hizuke_koumoku] = hizuke_df
        kabu_df[self.hizuke_koumoku] = pd.to_datetime(kabu_df[
            self.hizuke_koumoku])
        return kabu_df

    def kabuka_youbi_del(self, kabu_df, hizuke, hizuke_df):
        # 日付項目の曜日文字を削除
        hizuke_df = kabu_df[self.hizuke_koumoku]
        hizuke_df = hizuke.day_of_week_delete(hizuke_df)
        return hizuke_df

    # 株価データフレームの生成
    def cleateKabukaDf(self, kabuka_html):
        return pd.read_html(kabuka_html)

    # 株価取得ドライバの生成
    def newKabukaDriver(self):
        nw = Niltukei_web()
        return nw.cleate_driver()

    def getKabukaHtml(self, company_code, driver):
        nc = Niltukei_company()
        return nc.getCompanyHtml(company_code, driver)

    # 株値のhtml取得
    def searchKabukaHtml(self, driver):
        kabuka = WebDriverWait(driver, 10).until(lambda x: x.find_element(
            By.LINK_TEXT, Niltukei_const.HTML_KABUKA_SEARCH))
        kabuka.click()
        kabuka_table = WebDriverWait(driver, 10).until(
            lambda y: y.find_element(By.CLASS_NAME,
                                     Niltukei_const.HTML_W668_SEARCH))
        # table要素を含むhtmlを取得
        kabuka_html = kabuka_table.get_attribute(
            Niltukei_const.HTML_OUTER_HTML_SEARCH)
        return kabuka_html

    # 株値データフレームカラム変更
    def renameKabukaDfColumn(self, kabu_df):
        kabu_df = kabu_df.rename(columns={
            Niltukei_const.HIZEKE_KOUMOKU:
                Niltukei_const.HIZEKE_KOUMOKU,
            Niltukei_const.HAJIMARINE_KOUMOKU:
                Niltukei_const.HAJIMARINE_KOUMOKU,
            Niltukei_const.TAKENE_KOUMOKU:
                Niltukei_const.TAKENE_KOUMOKU,
            Niltukei_const.self.yasune_koumoku:
                Niltukei_const.YASUNE_KOUMOKU,
            Niltukei_const.OWARINE_KOUMOKU:
                Niltukei_const.OWARINE_KOUMOKU,
            Niltukei_const.URIKAIDAKA_KOUMOKU:
                Niltukei_const.URIKAIDAKA_KOUMOKU,
            Niltukei_const.SYUSEIGO_OWARINE_KOUMOKU:
                Niltukei_const.SYUSEIGO_OWARINE_KOUMOKU})
        return kabu_df

    def kabuka_taisyaku_init_set(self, file_name, file_path):
        self.kabuka_taisyaku_path = file_path
        self.kabuka_taisyaku_file_name = file_name

    # 企業名取得
    def getKabukaTitle(self, driver):
        nh = Niltukei_html()
        # self.kabuka_title = re.search(r'【(.+)】', driver.title).group(1)
        return nh.getHtmlTitle(driver)
