from niltukei_const import Niltukei_const
import config
import pandas as pd


class Ruseki:

    def readRuseki(self):
        return pd.read_csv(Niltukei_const.CSV_PATH
                           + config.title
                           + '_累積.csv')
