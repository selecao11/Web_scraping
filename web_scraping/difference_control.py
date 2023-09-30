from difference import Difference
from niltukei_html import Niltukei_html
from niltukei_const import Niltukei_const


class Difference_control:

    def dropDifferenceColum(self, df, niltukei_join_df):
        return df.dropColum(
            niltukei_join_df[niltukei_join_df["_merge"] == "right_only"])

    def renameDifferenceColum(self, df, niltukei_join_df):
        return df.renameColum(self.dropDifferenceColum(df, niltukei_join_df))

    def selectDifference(self, difference_dict, niltukei_join_df, driver):
        df = Difference()
        print(niltukei_join_df)
        difference_df = self.renameDifferenceColum(df, niltukei_join_df)
        nh = Niltukei_html()
        difference_df.to_csv(
            difference_dict["csv_path"]
            + nh.getHtmlTitle(driver)
            + Niltukei_const.FILE_NAME_DIFFERENCE)
        return difference_df
