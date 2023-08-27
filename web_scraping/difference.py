from  web_scraping.hizuke import Hizuke
import pandas as pd
import re


class Difference:

    merge_df = None
    difference_df = None

    def difference_init(self,merge_df):
        self.merge_df = merge_df

    def colum_drop(self):
        self.difference_df = self.difference_df.drop("Unnamed: 0", axis=1)

    def difference_select(self):
        self.difference_df = self.merge_df[self.merge_df["_merge"] == "left_only"]
        self.colum_drop()
        print(self.difference_df)
        return self.difference_df
