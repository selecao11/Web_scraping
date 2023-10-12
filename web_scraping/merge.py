import pandas as pd
from niltukei_html import Niltukei_html
from niltukei_const import Niltukei_const
import config

class Merge:

    merge_ruiseki_df = None
    merge_nikei_data_df = None
    merge_df = None

    merge_path = None
    merge_file_name = None
    merge_title = None
    '''
    def nikei_merge_init(self, ruiseki_df, nikei_data_df, file_path,
                         file_name, title):
        self.merge_ruiseki_df = ruiseki_df
        self.merge_nikei_data_df = nikei_data_df
        self.merge_path = file_path
        self.merge_file_name = file_name
        self.merge_title = title
    '''

    def colum_drop(self, merge_df):
        return merge_df

    def mergeNikei(self, ruikei_df, niltukei_join):
        ruikei_df["日付"] =\
            ruikei_df["日付"].astype("datetime64[ns]")
        merge_df = pd.merge(
            ruikei_df, niltukei_join,
            on=["日付"], how='outer', indicator=True)
        merge_df = self.colum_drop(merge_df)
        # merge_df.to_csv(csv_path + '/tests/三菱自動車_link_マージ.csv')
        merge_df = merge_df.drop("Unnamed: 0", axis=1)
        merge_df.to_csv(
            Niltukei_const.CSV_PATH
            + config.title
            + Niltukei_const.FILE_NAME_MEARGE)
        return merge_df
