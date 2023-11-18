from ruiseki import Ruseki
from ruseki_mismatch import RuisekiMismatch
from niltukei_const import Niltukei_const


class Ruseki_control:

    def readRuiseki(self):
        ru = Ruseki()
        return ru.readRuseki()

    def setMismatchRuikei(self, missmatch, data_frame):
        # 信用残の不一致
        """ データ取得漏れデータフレームの判断をする
        Args:
            missmatch (String): "貸株残", "融資残", "貸株残", "逆日歩", "日歩日数"
            data_frame (DataFrame): データ取得漏れデータフレーム
        Returns:
            missmatch_koumoku(DataFrame): 変更後の累積のデータフレーム
        """
        missmatch_koumoku = {}
        if Niltukei_const.SHINYOU_URI_KOUMOKU in data_frame.columns:
            if missmatch == Niltukei_const.SHINYOU_URI_KOUMOKU:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_SHINYOU_URI_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.SHINYOU_URI_KOUMOKU
            if missmatch == Niltukei_const.SHINYOU_KAI_KOUMOKU:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_SHINYOU_KAI_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.SHINYOU_KAI_KOUMOKU
            if missmatch == Niltukei_const.SHINYOU_BAI_KOUMOKU:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_SHINYOU_BAI_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.SHINYOU_BAI_KOUMOKU
        if Niltukei_const.KASHIKABU_ZAN in data_frame.columns:
            # 貸株残の不一致
            if missmatch == Niltukei_const.GYAKUHIBU_KOUMOKU:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_GYAKUHIBU_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.GYAKUHIBU_KOUMOKU
            if missmatch == Niltukei_const.HIBU_KOUMOKU:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_HIBU_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.HIBU_KOUMOKU
            if missmatch == Niltukei_const.KASHIKABU_ZAN:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_KASHIKABU_ZAN
                missmatch_koumoku["correct"] =\
                    Niltukei_const.KASHIKABU_ZAN
            if missmatch == Niltukei_const.YUSHI_ZAN_KOUMOKU:
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.YUSHI_ZAN_KOUMOKU
        return missmatch_koumoku

    def updataMismatchRuikei(self,
        company_code,
        gyakuhibu_driver,
        missmatch,
        ruiseki_df,
        data_frame):
        # shinyou_dict):
        """ 対象データフレームの項目と累積の項目で不一致の行を抽出し、
            累積の項目を上書きする
        Args:
            ruiseki_df (DataFrame): 累積のデータフレーム
            data_frame (DataFrame): 逆日歩のデータフレーム
        Returns:
            updata_ruiseki_df(DataFrame): 変更後の累積のデータフレーム
        """
        # 日付項目を64_NSに変更
        rm = RuisekiMismatch()
        ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU] = \
            ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU]\
            .astype(Niltukei_const.DATE_TIME64_NS)

        # データ取得もれの有無チェックの設定
        missmatch_koumoku = self.setMismatchRuikei(missmatch,
                                                   data_frame)
        # 逆日歩_貸株残と累積でデータ取得もれの有無のチェック
        ruiseki_mismatch_df = rm.getMismatchField(
            missmatch, missmatch_koumoku,
            ruiseki_df,
            data_frame)
        # 累積のデータ取得もれ発生日を抽出
        ruiseki_mismatch_days_df =\
            rm.getStockLendingMismatchDays(ruiseki_mismatch_df)
        # 逆日歩_貸株残から該当日データを抽出
        miss_match_day_data_frame =\
            rm.getGyakuStockLendingMismatchDays(missmatch,
                                                ruiseki_mismatch_days_df,
                                                data_frame)
        # 逆日歩_貸借桟の貸株残を累積に出力
        updata_ruiseki_df = \
            rm.updataRuisekiDay(missmatch, ruiseki_df,
                                miss_match_day_data_frame)

        return updata_ruiseki_df
    