import pandas as pd
from niltukei_html import Niltukei_html


class Ruseki:

    def readRuseki(self, csv_path, driver):
        nh = Niltukei_html()
        return pd.read_csv(csv_path
                           + nh.getHtmlTitle(driver) + '_累積.csv')
