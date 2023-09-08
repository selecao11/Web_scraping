import pandas as pd
from niltukei_const import Niltukei_const


class test_gyakuhibu_taisyaku_comp:
    CSV_PATH = "/home/user/anaconda3/envs/web_scraping/web_scraping/csv/"
    gyaku_df = None
    ruiseki_df = None
    ruiseki_Non_stock_lending_df = None
    gyakuhibu_day_df = None
    stock_load_balance = None

    def __init__(self) -> None:
        self.gyaku_df = pd.read_csv(self.CSV_PATH + 'スノーピーク_累積.csv')

    # 逆日歩_貸株残と累積でデータ誤差の有無のチェック
    def NotContain_stock_lending(self, diff_days):
        self.gyakuhibu_day_df = \
            self.gyaku_df[self.gyaku_df[Niltukei_const.HIZEKE_KOUMOKU]
                          .isin(diff_days)]

    def SetRuisekiDfStockLoadBalance(self, i_list):
        for i, v in enumerate(i_list):
            print(i)
            self.ruiseki_df.loc[v, '累積貸株残'] = self.stock_load_balance[i]
        return self.ruiseki_df

    # 逆日歩_貸株残の貸株残をセット
    def SetStockLendingDay(self):
        self.stock_load_balance = self.gyakuhibu_day_df.loc[:, '貸株残'].values

    def AddStockLendingDay(self, ruiseki_df, ruiseki_disagreement_days):
        '''
            逆日歩_貸株残の貸株残が不一致の日を抽出

            :param data frame:ruiseki_df                :累積のデータフレーム
            :param List:ruiseki_disagreement_days       :累積のデータフレーム
            :return  data frame:gyaku_disagreement_days :逆日歩の不一日のリスト
        '''
        gyaku_disagreement_days = list()
        for day in ruiseki_disagreement_days:
            gyaku_disagreement_days\
                .append(ruiseki_df.index[ruiseki_df[Niltukei_const
                                                    .HIZEKE_KOUMOKU] == day])
        self.SetStockLendingDay()
        return gyaku_disagreement_days

    def GetStocklending(self, ruiseki_Non_stock_lending_df):
        '''
            累積の累積貸株残が不一致の行から日付を抽出

            :param Dataframe    :ruiseki_Non_stock_lending_df   :累積のデータフレーム
            :return  List       :ruiseki_disagreement_days      :累積の不一日のリスト
        '''
        ruiseki_disagreement_days = list()
        for day in ruiseki_Non_stock_lending_df[Niltukei_const
                                                .HIZEKE_KOUMOKU]:
            ruiseki_disagreement_days.append(day.strftime('%Y-%m-%d'))
        return ruiseki_disagreement_days

    def GetStockLendingBalanceDay(self, ruiseki_df, gyaku_df):
        '''
            逆日歩の貸株残と累積の貸株残で不一致の行を抽出

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
        ruiseki_Non_stock_lending_df = \
            self.ruiseki_df[~ruiseki_df[Niltukei_const
                            .RUISEKI_KASHIKABU_ZAN]
                            .isin(gyaku_df[Niltukei_const
                                           .RUISEKI_KASHIKABU_ZAN])]
        return ruiseki_Non_stock_lending_df

    def Comp_gyakuhibu_taisyakuzan_ruiseki(self, ruiseki_df, gyaku_df):
        '''
            逆日歩の貸株残と累積の累積貸株残で不一致の行を抽出し、
            貸株残で累積貸株残を上書きする

                param
            ---------------
            ruiseki_df                  : data frame
                累積のデータフレーム
            gyaku_df                    : data frame
                逆日歩のデータフレーム

                return
            ---------------
            ruiseki_df                  :data frame
                変更後の累積のデータフレーム
        '''
        ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU] = \
            self.ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU]\
                .astype(Niltukei_const.DATE_TIME64_NS)
        # 逆日歩_貸株残と累積でデータ誤差の有無のチェック
        self.NotContain_stock_lending()
        # 累積のデータ誤差発生日を抽出
        ruiseki_disagreement_days = self.GetStocklending()
        # 逆日歩_貸株残の該当日データを抽出
        self.GetStockLendingBalanceDay(ruiseki_disagreement_days)
        # 逆日歩_貸借桟の貸株残を累積に出力
        gyaku_disagreement_days = \
            self.AddStockLendingDay(ruiseki_disagreement_days)
        self.ruiseki_df = \
            self.SetRuisekiDfStockLoadBalance(gyaku_disagreement_days)
        self.ruiseki_df.to_csv(self.CSV_PATH + 'shinyou_zan_df_comp.csv')
        return ruiseki_df


gt = test_gyakuhibu_taisyaku_comp()
ruiseki_df = gt.Comp_gyakuhibu_taisyakuzan_ruiseki()
