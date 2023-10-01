import pandas as pd
from web_scraping.niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html


class RuisekiMismatch:
    gyaku_df = None
    ruiseki_df = None
    ruiseki_Non_stock_lending_df = None
    gyakuhibu_day_df = None
    stock_load_balance = None

    def saveMismatchRuseki(self, csv_path, updata_ruiseki_df, ruiseki_df,
                           driver):
        nh = Niltukei_html()
        updata_ruiseki_df.to_csv(csv_path
                                 + nh.getHtmlTitle(driver)
                                 + '累積_更新後.csv')
        ruiseki_df.to_csv(csv_path
                          + nh.getHtmlTitle(driver)
                          + '累積_更新前.csv')

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

    def updataRuisekiDay(self, ruiseki_df, gyaku_mismatch_df):
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
        ruiseki_df = ruiseki_df.fillna(0)
        for _, row in gyaku_mismatch_df.iterrows():
            ruiseki_df.loc[
                ruiseki_df[
                    Niltukei_const.HIZEKE_KOUMOKU
                ] == row[Niltukei_const.HIZEKE_KOUMOKU],
                Niltukei_const.RUISEKI_KASHIKABU_ZAN
            ] = row[Niltukei_const.KASHIKABU_ZAN]

        return ruiseki_df

    def getGyakuStockLendingMismatchDays(self, ruiseki_disagreement_days,
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
        return gyaku_disagreement_days_df[
                [
                    Niltukei_const.HIZEKE_KOUMOKU,
                    Niltukei_const.KASHIKABU_ZAN,
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

    def getMismatchLoanStumpRec(self, ruiseki_df, gyaku_df):
        '''
            逆日歩の貸株残と累積の貸株残で不一致の行を抽出

                param
            ---------------
            ruiseki_df                        : data frame
                累積のデータフレーム
            gyaku_df                            : data frame
                逆日歩のデータフレーム

                return
            ---------------
            ruiseki_Mismatch_df        :data frame
                累積の不一致行
        '''
        ruiseki_mismatch_df = \
            ruiseki_df[
                ~ruiseki_df[Niltukei_const.RUISEKI_KASHIKABU_ZAN].isin(
                    gyaku_df[Niltukei_const.KASHIKABU_ZAN])
            ]
        # print(ruiseki_mismatch_df.dtypes)
        return ruiseki_mismatch_df

