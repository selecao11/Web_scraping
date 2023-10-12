from difference import Difference
from niltukei_html import Niltukei_html
from niltukei_const import Niltukei_const
import config

class Difference_control:

    def dropDifferenceColum(self, df, niltukei_join_df):
        return df.dropColum(
            niltukei_join_df[niltukei_join_df["_merge"] == "right_only"])

    def renameDifferenceColum(self, df, niltukei_join_df):
        return df.renameColum(self.dropDifferenceColum(df, niltukei_join_df))

    def selectDifference(self, niltukei_join_df):
        df = Difference()
        difference_df = self.renameDifferenceColum(df, niltukei_join_df)
        difference_df.to_csv(
            Niltukei_const.CSV_PATH
            + config.title
            + Niltukei_const.FILE_NAME_DIFFERENCE)
        return difference_df
