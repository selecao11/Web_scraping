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
            self.gyaku_df[self.gyaku_df['日付'].isin(diff_days)]

    def SetRuisekiDfStockLoadBalance(self, i_list):
        for i, v in enumerate(i_list):
            print(i)
            self.ruiseki_df.loc[v, '累積貸株残'] = self.stock_load_balance[i]
        return self.ruiseki_df

    # 逆日歩_貸株残の貸株残をセット
    def SetStockLendingDay(self):
        self.stock_load_balance = self.gyakuhibu_day_df.loc[:, '貸株残'].values

    # 逆日歩_貸株残の不一致日を抽出
    def AddStockLendingDay(self, diff_days):
        gyaku_disagreement_days = list()
        for day in diff_days:
            gyaku_disagreement_days\
                .append(self.ruiseki_df.index[self.ruiseki_df['日付'] == day])
        self.SetStockLendingDay()
        return gyaku_disagreement_days

    # 累積の不一致の行の日付を抽出
    def GetStocklending(self):
        ruiseki_disagreement_days = list()
        for day in self.ruiseki_Non_stock_lending_df["日付"]:
            ruiseki_disagreement_days.append(day.strftime('%Y-%m-%d'))
        return ruiseki_disagreement_days

    def GetStockLendingBalanceDay(self, ruiseki_df, gyaku_df):
        '''
            逆日歩の貸株残と累積の貸株残で不一致の行を抽出

            :param ruiseki_df:累積のデータフレーム
            :param gyaku_df:逆日歩のデータフレーム
            :return  data frame ruiseki_Non_stock_lending_df:累積の不一致行
        '''
        ruiseki_Non_stock_lending_df = \
            self.ruiseki_df[~ruiseki_df['累積貸株残'].isin(gyaku_df['貸株残'])]
        return ruiseki_Non_stock_lending_df

    def Comp_gyakuhibu_taisyakuzan_ruiseki(self):
        '''
            逆日歩の貸株残と累積の貸株残で不一致の行を抽出
        :
        '''
        self.ruiseki_df[Niltukei_const.HIZEKE_KOUMOKU] = \
            self.ruiseki_df["日付"].astype(Niltukei_const.DATE_TIME64_NS)
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


tg = test_gyakuhibu_taisyaku_comp()
tg.Comp_gyakuhibu_taisyakuzan_ruiseki()
