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
    def cleateKabukadf(self, company_code):
        kb = Kabuka()
        file_name = Niltukei_const.FILE_NAME_KABUKA
        # kb.kabuka_title_get(Kabuka_dict['driver'])
        '''
        kb.kabuka_taisyaku_init_set(
            file_name, kabuka_dict[Niltukei_const.DICT_CSV_PATH])
        '''
        hizuke = Hizuke()
        dd = kb.getKabukaHtml(company_code, kb.newKabukaDriver())
        kabuka_html = kb.searchKabukaHtml(
            dd
            )
        kabuka_df = kb.cleateKabukaDf(kabuka_html)
        kabu_df = kabuka_df[0]
        # 株値データフレームのカラム名の変更
        # kabu_df = kb.renameKabukaDfColumn(kabu_df)
        hizuke_df = kabu_df[Niltukei_const.HIZEKE_KOUMOKU]
        """
        test
        kabu_df['曜日'] = kabu_df['日付'].str.extract(r'(?<=\().+?(?=\))')
        """
        # 株値データフレームの日付項目の曜日を削除
        hizuke_df = kb.kabuka_youbi_del(kabu_df, hizuke, hizuke_df)
        # 株値データフレームの日付項目の月日に年を追加
        kabu_df = kb.kabuka_hizuke_yy_add(kabu_df, hizuke, hizuke_df)
        # 取得したデータを取得株値として記録
        nh = Niltukei_html()
        kabu_df.to_csv(Niltukei_const.CSV_PATH
                       + nh.getHtmlTitle(
                           kb.getKabukaHtml(
                                company_code,
                                kb.newKabukaDriver())
                        )
                       + Niltukei_const.FILE_NAME_KABUKA)
        return kabu_df
