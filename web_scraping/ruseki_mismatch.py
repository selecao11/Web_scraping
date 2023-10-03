import pandas as pd
from web_scraping.niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html


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

    def saveMismatchRuseki(self, csv_path, updata_ruiseki_df,
                           driver):
        nh = Niltukei_html()
        updata_ruiseki_df.to_csv(csv_path
                                 + nh.getHtmlTitle(driver)
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

    def updataRuisekiDay(self, missmatch, ruiseki_df, gyaku_mismatch_df):
        '''
            累積の不一致日の貸株残を逆日歩_貸株残の貸株残で更新する
                param
            ---------------
            ruiseki_df                          : DataFrame
                            累積のデータフレーム
            gyaku_mismatch_df                     : DataFrame
                            逆日歩の不一致データフレーム
                return
            ---------------
            ruiseki_df                          : DataFrame
                            累積のデータフレーム
        '''
        if missmatch == "貸株残":
            missmatch_koumoku_ruiseki = Niltukei_const.RUISEKI_KASHIKABU_ZAN
            missmatch_koumoku_gyaku = Niltukei_const.KASHIKABU_ZAN
        if missmatch == "融資残":
            missmatch_koumoku_ruiseki =\
                Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU
            missmatch_koumoku_gyaku = Niltukei_const.YUSHI_ZAN_KOUMOKU
        ruiseki_df = ruiseki_df.fillna(0)
        for _, row in gyaku_mismatch_df.iterrows():
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
                                         gyaku_df):
        '''
            累積の不一致の日を参考に逆日歩_貸株残の不一致日を抽出

                param
            ---------------
            ruiseki_disagreement_days        : List
                累積の不一致日データフレーム

                return
            ---------------
            gyaku_disagreement_days_df        :List
                逆日歩の不一致行
        '''
        gyaku_disagreement_days_df = pd.merge(
            gyaku_df,
            ruiseki_disagreement_days,
            left_on=Niltukei_const.HIZEKE_KOUMOKU,
            right_on=Niltukei_const.HIZEKE_KOUMOKU
            )
        if missmatch == "貸株残":
            missmatch_koumoku_gyaku = Niltukei_const.KASHIKABU_ZAN
        if missmatch == "融資残":
            missmatch_koumoku_gyaku = Niltukei_const.YUSHI_ZAN_KOUMOKU
        return gyaku_disagreement_days_df[
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

    def getMismatchField(self, missmatch_koumoku, ruiseki_df, data_frame):
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

