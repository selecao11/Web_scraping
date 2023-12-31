import pandas as pd
# from niltukei_html import Niltukei_html
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
        """ 結合データフレームを比較判断して差分データにleft_onlyをつける
        Args:
            ruikei_df (DataFrame): 累積データフレーム
            niltukei_join (DataFrame): 結合データフレーム
        Returns:
            merge_df(DataFrame): 比較判断したデータフレーム
        """
        ruikei_df[Niltukei_const.HIZEKE_KOUMOKU] =\
            ruikei_df[Niltukei_const.HIZEKE_KOUMOKU].astype(
                Niltukei_const.DATE_TIME64_NS)
        merge_df = pd.merge(
            ruikei_df, niltukei_join,
            on=[Niltukei_const.HIZEKE_KOUMOKU], how='outer', indicator=True)
        merge_df = self.colum_drop(merge_df)
        merge_df = merge_df.drop(Niltukei_const.UNNAMED_0_KOUMOKU, axis=1)
        merge_df.to_csv(
            Niltukei_const.CSV_PATH
            + config.title
            + Niltukei_const.FILE_NAME_MEARGE)
        return merge_df
