from ruiseki import Ruseki
from ruseki_mismatch import RuisekiMismatch
from niltukei_const import Niltukei_const


class Ruseki_control:

    def readRuiseki(self, csv_path, driver):
        ru = Ruseki()
        return ru.readRuseki(csv_path, driver)

    def setMismatchRuikei(self, missmatch, data_frame):
        # 信用残の不一致
        missmatch_koumoku = {}
        if "信用売残" in data_frame.columns:
            if missmatch == "信用売残":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_SHINYOU_URI_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.SHINYOU_URI_KOUMOKU
            if missmatch == "信用買残":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_SHINYOU_KAI_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.SHINYOU_KAI_KOUMOKU
            if missmatch == "信用倍率":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_SHINYOU_BAI_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.SHINYOU_BAI_KOUMOKU
        if "貸株残" in data_frame.columns:
            # 貸株残の不一致
            if missmatch == "逆日歩":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_GYAKUHIBU_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.GYAKUHIBU_KOUMOKU
            if missmatch == "日歩日数":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_HIBU_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.HIBU_KOUMOKU
            if missmatch == "貸株残":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_KASHIKABU_ZAN
                missmatch_koumoku["correct"] =\
                    Niltukei_const.KASHIKABU_ZAN
            if missmatch == "融資残":
                missmatch_koumoku["ruiseki"] =\
                    Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU
                missmatch_koumoku["correct"] =\
                    Niltukei_const.YUSHI_ZAN_KOUMOKU
        return missmatch_koumoku

    def updataMismatchRuikei(self, missmatch,
                             ruiseki_df,
                             data_frame,
                             shinyou_dict):
        '''
            対象データフレームの項目と累積の項目で不一致の行を抽出し、
            累積の項目を上書きする

                param
            ---------------
            ruiseki_df                  : data frame
                累積のデータフレーム
            data_frame                    : data frame
                逆日歩のデータフレーム

                return
            ---------------
            ruiseki_df                  :data frame
                変更後の累積のデータフレーム
        '''
        # 日付項目を64_NSに変更
        rm = RuisekiMismatch()
        ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU] = \
            ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU]\
            .astype(Niltukei_const.DATE_TIME64_NS)

        # データ誤差の有無チェックの必要設定
        missmatch_koumoku = self.setMismatchRuikei(missmatch, data_frame)
        # 逆日歩_貸株残と累積でデータ誤差の有無のチェック
        ruiseki_mismatch_df = rm.getMismatchField(
            missmatch, missmatch_koumoku, ruiseki_df, data_frame)
        # 累積のデータ誤差発生日を抽出
        ruiseki_mismatch_days_df =\
            rm.getStockLendingMismatchDays(ruiseki_mismatch_df)
        # 逆日歩_貸株残の該当日データを抽出
        miss_match_day_data_frame =\
            rm.getGyakuStockLendingMismatchDays(missmatch,
                                                ruiseki_mismatch_days_df,
                                                data_frame)
        # 逆日歩_貸借桟の貸株残を累積に出力
        updata_ruiseki_df = \
            rm.updataRuisekiDay(missmatch, ruiseki_df,
                                miss_match_day_data_frame)
        csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"\
            "web_scraping/Cumulative_stock_price_data/"
        driver = shinyou_dict["driver"]
        return rm.saveMismatchRuseki(csv_path,
                                     rm.dropRuseki(updata_ruiseki_df),
                                     driver)
