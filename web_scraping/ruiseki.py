from niltukei_const import Niltukei_const
import config
import pandas as pd


class Ruseki:

    def readRuseki(self):
        return pd.read_csv(Niltukei_const.CSV_PATH
                           + config.title
                           + '_累積.csv')

    def resetIndexRuseki(self, ruiseki_df):
        return ruiseki_df.reindex(columns=["日付",
                                           "曜日",
                                           "週",
                                           "累積始値",
                                           "累積高値",
                                           "累積安値",
                                           "累積終値",
                                           "累積売買高",
                                           "累積修正後終値",
                                           "累積信用売残",
                                           "累積信用買残",
                                           "累積信用倍率",
                                           "累積逆日歩",
                                           "累積日歩日数",
                                           "累積貸株残",
                                           "累積融資残"
                                           ])


