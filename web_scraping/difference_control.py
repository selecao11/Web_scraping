from difference import Difference
from niltukei_html import Niltukei_html
from niltukei_const import Niltukei_const


class Difference_control:

    def dropDifferenceColum(self, df, niltukei_join_df):
        return df.colum_drop(
            niltukei_join_df[niltukei_join_df["_merge"] == "right_only"])

    def renameDifferenceColum(self, df, niltukei_join_df):
        return df.colum_rename(self.dropDifferenceColum(df, niltukei_join_df))

    def selectDifference(self, difference_dict, niltukei_join_df, driver):
        df = Difference()
        print(niltukei_join_df)
        difference_df = self.renameDifferenceColum(df, niltukei_join_df)
        nh = Niltukei_html()
        difference_df.to_csv(
            difference_dict["csv_path"]
            + nh.get_html_title(driver)
            + Niltukei_const.FILE_NAME_DIFFERENCE)
        return difference_df
