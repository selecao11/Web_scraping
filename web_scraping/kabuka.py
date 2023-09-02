from  hizuke import Hizuke
import pandas as pd
import re

class Kabuka:

    hizuke_koumoku='日付'
    hajimarine_koumoku='始値'
    takane_koumoku='高値'
    yasune_koumoku='安値'
    owarine_koumoku='終値'
    urikaidaka_koumoku='売買高'
    syuseigoatai_koumoku='修正後終値'
    kabuka_koumoku = '株価'

    kabuka_title = None
    kabuka_taisyaku_path = None
    kabuka_taisyaku_file_name = None

    def kabuka_hizuke_yy_add(self,kabu_df,hizuke,hizuke_df):
        #日付項目の月日に年を追加
        hizuke_df = hizuke.year_add(hizuke_df)
        kabu_df[self.hizuke_koumoku] = hizuke_df
        kabu_df[self.hizuke_koumoku] = pd.to_datetime(kabu_df[self.hizuke_koumoku])
        return kabu_df

    def kabuka_youbi_del(self,kabu_df,hizuke,hizuke_df):
        #日付項目の曜日文字を削除
        hizuke_df = kabu_df[self.hizuke_koumoku]
        hizuke_df = hizuke.day_of_week_delete(hizuke_df)
        return hizuke_df

    #株値のhtml取得
    def kabuka_html_search(self,WebDriverWait,driver,By):
        kabuka = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.LINK_TEXT, self.kabuka_koumoku))
        kabuka.click()
        kabuka_table = WebDriverWait(driver, 10).until(lambda y: y.find_element(By.CLASS_NAME, "w668"))
        kabuka_html=kabuka_table.get_attribute("outerHTML") #table要素を含むhtmlを取得
        return kabuka_html

    #株値データフレームカラム変更
    def kabuka_df_rename(self,kabu_df):
        kabu_df = kabu_df.rename(columns={  self.hizuke_koumoku:self.hizuke_koumoku,\
                                            self.hajimarine_koumoku:self.hajimarine_koumoku,\
                                            self.takane_koumoku:self.takane_koumoku,\
                                            self.yasune_koumoku:self.yasune_koumoku,\
                                            self.owarine_koumoku:self.owarine_koumoku,\
                                            self.urikaidaka_koumoku:self.urikaidaka_koumoku,
                                            self.syuseigoatai_koumoku:self.syuseigoatai_koumoku})
        return kabu_df

    def kabuka_taisyaku_init_set(self,file_name,file_path):
        self.kabuka_taisyaku_path = file_path
        self.kabuka_taisyaku_file_name = file_name

    #企業名取得    
    def kabuka_title_get(self,driver):    
        self.kabuka_title = re.search(r'【(.+)】',driver.title).group(1)
        return self.kabuka_title

    #株値取得
    def kabuka_df_cleate(self,WebDriverWait,driver,pd,By):
        hizuke = Hizuke()
        kabuka_html = self.kabuka_html_search(WebDriverWait,driver,By)
        kabuka_df=pd.read_html(kabuka_html) #tableをDataFrameに格納
        kabu_df = kabuka_df[0]
        #株値データフレームのカラム名の変更
        kabu_df = self.kabuka_df_rename(kabu_df)
        print(type(kabu_df))
        hizuke_df = kabu_df[self.hizuke_koumoku]
        #株値データフレームの日付項目の曜日を削除
        hizuke_df = self.kabuka_youbi_del(kabu_df,hizuke,hizuke_df)
        #株値データフレームの日付項目の月日に年を追加
        kabu_df = self.kabuka_hizuke_yy_add(kabu_df,hizuke,hizuke_df)
        #取得したデータを取得株値として記録
        kabu_df.to_csv(self.kabuka_taisyaku_path + self.kabuka_title + self.kabuka_taisyaku_file_name)
        return kabu_df
