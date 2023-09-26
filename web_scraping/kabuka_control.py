from hizuke import Hizuke
from kabuka import Kabuka
from niltukei_const import Niltukei_const


class Kabuka_control:
    # 株値取得
    def cleate_kabuka_df(self, WebDriverWait, driver, pd,  By):
        kb = Kabuka()
        file_name = Niltukei_const.FILE_NAME_KABUKA
        kb.kabuka_title_get(self.driver)
        kb.kabuka_taisyaku_init_set(file_name, self.csv_path)
        self.title = kb.kabuka_title_get(self.driver)
        #
        h = Hizuke()
        kabuka_html = self.kabuka_html_search(WebDriverWait, driver, By)
        # tableをDataFrameに格納
        self.kabu_df = kb.kabuka_df_cleate(WebDriverWait, self.driver, pd, By)
        kabuka_df = pd.read_html(kabuka_html)
        kabu_df = kabuka_df[0]
        # 株値データフレームのカラム名の変更
        kabu_df = self.kabuka_df_rename(kabu_df)
        hizuke_df = kabu_df[self.hizuke_koumoku]
        # 株値データフレームの日付項目の曜日を削除
        hizuke_df = self.kabuka_youbi_del(kabu_df, h, hizuke_df)
        # 株値データフレームの日付項目の月日に年を追加
        kabu_df = self.kabuka_hizuke_yy_add(kabu_df, h, hizuke_df)
        # 取得したデータを取得株値として記録
        kabu_df.to_csv(self.kabuka_taisyaku_path + self.kabuka_title
                       + self.kabuka_taisyaku_file_name)
        return kabu_df
