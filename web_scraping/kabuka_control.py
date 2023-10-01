from hizuke import Hizuke
from kabuka import Kabuka
from niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html


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
        kb.kabuka_taisyaku_init_set(
            file_name, kabuka_dict[Niltukei_const.DICT_CSV_PATH])
        #
        h = Hizuke()
        kabuka_html = kb.kabuka_html_search(
            kabuka_dict[Niltukei_const.DICT_WEB_DRIVER],
            kabuka_dict[Niltukei_const.DICT_DRIVER],
            kabuka_dict[Niltukei_const.DICT_COMMON_BY])
        pd = kabuka_dict[Niltukei_const.DICT_PANDAS]
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
        nh = Niltukei_html()
        kabu_df.to_csv(kb.kabuka_taisyaku_path
                       + nh.getHtmlTitle(driver)
                       + kb.kabuka_taisyaku_file_name)
        return kabu_df
