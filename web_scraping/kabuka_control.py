from hizuke import Hizuke
from kabuka import Kabuka
from niltukei_const import Niltukei_const
# from niltukei_html import Niltukei_html
# import re
import config


class Kabuka_control:

    # 株値取得
    def cleateKabukadf(self, company_code):
        """ 株値データフレームの生成を行う

        Args:
            company_code (string): 日経ページの企業コード

        Returns:
            kabu_df(dataframe): 株価取得データフレーム
        """
        kb = Kabuka()
        hizuke = Hizuke()
        # 該当企業の株値のページの取得
        kabuka_Driver = kb.getKabukaHtml(company_code, kb.newKabukaDriver())
        # 株値のページ内でデータ部分の検索
        kabuka_html = kb.searchKabukaHtml(
            kabuka_Driver
            )
        # 使用済のドライバの開放
        kb.delKabukaDriver(kabuka_Driver)
        # 取得したテーブルから株価データフレームの生成
        kabuka_df = kb.cleateKabukaDf(kabuka_html)
        kabu_df = kabuka_df[0]
        # 株値データフレームのカラム名の変更
        kabu_df = kb.renameKabukaDfColumn(kabu_df)
        hizuke_df = kabu_df[Niltukei_const.HIZEKE_KOUMOKU]
        # 株値データフレームの日付項目の曜日を削除
        hizuke_df = kb.delKabukaDayOfWeek(kabu_df, hizuke, hizuke_df)
        # 株値データフレームの日付項目の月日に年を追加
        kabu_df = kb.addKabukaYear(kabu_df, hizuke, hizuke_df)
        # 取得したデータを取得株値のCSVファイルとして記録
        kabu_df.to_csv(Niltukei_const.CSV_PATH
                       + config.title
                       + Niltukei_const.FILE_NAME_KABUKA)
        return kabu_df
