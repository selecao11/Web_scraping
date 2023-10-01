from hizuke import Hizuke
from kabuka import Kabuka
from niltukei_const import Niltukei_const


class Kabuka_control:

    # ページタイトル取得
    def getKabukaHtmlTitle(self, driver):
        kb = Kabuka()
        return kb.getKabukaTitle(driver)

    # 株値取得
    def cleateKabukadf(self, kabuka_dict, driver):
        kb = Kabuka()
        file_name = Niltukei_const.FILE_NAME_KABUKA
        # kb.kabuka_title_get(Kabuka_dict['driver'])
        kb.kabuka_taisyaku_init_set(file_name, kabuka_dict['csv_path'])
        #
        h = Hizuke()
        kabuka_html = kb.kabuka_html_search(
            kabuka_dict['WebDriverWait'], kabuka_dict['driver'],
            kabuka_dict['By'])
        # tableをDataFrameに格納
        """
         self.kabu_df = kb.kabuka_df_cleate(
            Kabuka_dict['WebDriverWait'], Kabuka_dict['driver'],
            Kabuka_dict['By'], Kabuka_dict['pd'])
        """
        pd = kabuka_dict['pd']
        kabuka_df = pd.read_html(kabuka_html)
        kabu_df = kabuka_df[0]
        # 株値データフレームのカラム名の変更
        kabu_df = kb.kabuka_df_rename(kabu_df)
        hizuke_df = kabu_df[Niltukei_const.HIZEKE_KOUMOKU]
        # 株値データフレームの日付項目の曜日を削除
        hizuke_df = kb.kabuka_youbi_del(kabu_df, h, hizuke_df)
        # 株値データフレームの日付項目の月日に年を追加
        kabu_df = kb.kabuka_hizuke_yy_add(kabu_df, h, hizuke_df)
        # 取得したデータを取得株値として記録
        kabu_df.to_csv(kb.kabuka_taisyaku_path + kabuka_dict['title']
                       + kb.kabuka_taisyaku_file_name)
        return kabu_df
