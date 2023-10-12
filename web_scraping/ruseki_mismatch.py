import pandas as pd
from web_scraping.niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html
import config


class RuisekiMismatch:
    gyaku_df = None
    ruiseki_df = None
    ruiseki_Non_stock_lending_df = None
    gyakuhibu_day_df = None
    stock_load_balance = None

    def dropRuseki(self, updata_ruiseki_df):
        if 'Unnamed:' in updata_ruiseki_df.columns:
            updata_ruiseki_df = updata_ruiseki_df.drop('Unnamed: 0.1', axis=1)
            return updata_ruiseki_df
        else:
            return updata_ruiseki_df

    def saveMismatchRuseki(self, updata_ruiseki_df):
        updata_ruiseki_df.to_csv(Niltukei_const.CSV_PATH
                                 + config.title
                                 + '_累積.csv', index=False)
        return updata_ruiseki_df

    def getMismatchLoanBalanceRec(self, ruiseki_df, gyaku_df):
        '''
            逆日歩の融資残と累積の融資残で不一致の行を抽出

                param
            ---------------
            ruiseki_df                  : data frame
                累積のデータフレーム
            gyaku_df                            : data frame
                逆日歩のデータフレーム

                return
            ---------------
            ruiseki_Non_stock_lending_df        :data frame
                累積の不一致行
        '''
        ruiseki_Non_Loan_Balance_df = \
            ruiseki_df[
                ~ruiseki_df[Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU].isin(
                            gyaku_df[Niltukei_const.YUSHI_ZAN_KOUMOKU])
            ]
        return ruiseki_Non_Loan_Balance_df

    def updataRuisekiDay(self, missmatch, ruiseki_df,
                         miss_match_day_data_frame):
        '''
            累積の不一致日の貸株残を逆日歩_貸株残の貸株残で更新する
                param
            ---------------
            ruiseki_df                          : DataFrame
                            累積のデータフレーム
            miss_match_day_data_frame           : DataFrame
                            逆日歩の不一致データフレーム
                return
            ---------------
            ruiseki_df                          : DataFrame
                            累積のデータフレーム

        '''
        if missmatch == "逆日歩":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_GYAKUHIBU_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.GYAKUHIBU_KOUMOKU
        if missmatch == "日歩日数":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_HIBU_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.HIBU_KOUMOKU
        if missmatch == "貸株残":
            missmatch_koumoku_ruiseki = Niltukei_const.RUISEKI_KASHIKABU_ZAN
            missmatch_koumoku_gyaku = Niltukei_const.KASHIKABU_ZAN
        if missmatch == "融資残":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.YUSHI_ZAN_KOUMOKU
        if missmatch == "信用売残":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_SHINYOU_URI_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.SHINYOU_URI_KOUMOKU
        if missmatch == "信用買残":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_SHINYOU_KAI_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.SHINYOU_KAI_KOUMOKU
        if missmatch == "信用倍率":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_SHINYOU_BAI_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.SHINYOU_BAI_KOUMOKU

        ruiseki_df = ruiseki_df.fillna(0)
        for _, row in miss_match_day_data_frame.iterrows():
            ruiseki_df.loc[
                ruiseki_df[
                    Niltukei_const.HIZEKE_KOUMOKU
                ] == row[Niltukei_const.HIZEKE_KOUMOKU],
                missmatch_koumoku_ruiseki
            ] = row[missmatch_koumoku_gyaku]

        return ruiseki_df

    def getGyakuStockLendingMismatchDays(self,
                                         missmatch,
                                         ruiseki_disagreement_days,
                                         data_frame):
        '''
            累積の不一致の日を参考に逆日歩_貸株残の不一致日を抽出

                param
            ---------------
            ruiseki_disagreement_days        : List
                累積の不一致日データフレーム

                return
            ---------------
            miss_match_day_data_frame        :List
                逆日歩の不一致行
        '''
        miss_match_day_data_frame = pd.merge(
            data_frame,
            ruiseki_disagreement_days,
            left_on=Niltukei_const.HIZEKE_KOUMOKU,
            right_on=Niltukei_const.HIZEKE_KOUMOKU
            )
        if missmatch == "信用売残":
            missmatch_koumoku_gyaku = Niltukei_const.SHINYOU_URI_KOUMOKU
        if missmatch == "信用買残":
            missmatch_koumoku_gyaku = Niltukei_const.SHINYOU_KAI_KOUMOKU
        if missmatch == "信用倍率":
            missmatch_koumoku_gyaku = Niltukei_const.SHINYOU_BAI_KOUMOKU
        if missmatch == "逆日歩":
            missmatch_koumoku_gyaku = Niltukei_const.GYAKUHIBU_KOUMOKU
        if missmatch == "日歩日数":
            missmatch_koumoku_gyaku = Niltukei_const.HIBU_KOUMOKU
        if missmatch == "貸株残":
            missmatch_koumoku_gyaku = Niltukei_const.KASHIKABU_ZAN
        if missmatch == "融資残":
            missmatch_koumoku_gyaku = Niltukei_const.YUSHI_ZAN_KOUMOKU
        return miss_match_day_data_frame[
                [
                    Niltukei_const.HIZEKE_KOUMOKU,
                    missmatch_koumoku_gyaku,
                ]
        ]

    def getStockLendingMismatchDays(self, ruiseki_mismatch_df):
        '''
            累積のデータフレームから累積貸株残が不一致の日付を抽出

                param
            ---------------
            ruiseki_mismatch_df                 : data frame
                累積のデータフレーム

                return
            ---------------
            ruiseki_disagreement_days           :List
                累積の不一致行
        '''
        ruiseki_disagreement_days = list()
        for day in ruiseki_mismatch_df[Niltukei_const.HIZEKE_KOUMOKU]:
            ruiseki_disagreement_days.append(day)
        return pd.DataFrame(ruiseki_disagreement_days, columns=["日付"],
                            dtype=Niltukei_const.DATE_TIME64_NS)

    def getMismatchField(self, missmatch, missmatch_koumoku, ruiseki_df,
                         data_frame):
        '''
            逆日歩の貸株残と累積の貸株残で不一致の行を抽出

                param
            ---------------
            ruiseki_df                        : data frame
                累積のデータフレーム
            data_frame                            : data frame
                処理中のデータフレーム

                return
            ---------------
            ruiseki_mismatch_dict               :List
                貸株残、融資残の不一致データフレーム格納
        '''
        ruiseki_mismatch_df = \
            ruiseki_df[
                ~ruiseki_df[missmatch_koumoku["ruiseki"]].isin(
                    data_frame[missmatch_koumoku["correct"]])
            ]
        return ruiseki_mismatch_df

