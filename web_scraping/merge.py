import pandas as pd


class Merge:

    merge_ruiseki_df = None
    merge_nikei_data_df = None
    merge_df = None

    merge_path = None
    merge_file_name = None
    merge_title = None

    def nikei_merge_init(self, ruiseki_df, nikei_data_df, file_path,
                         file_name, title):
        self.merge_ruiseki_df = ruiseki_df
        self.merge_nikei_data_df = nikei_data_df
        self.merge_path = file_path
        self.merge_file_name = file_name
        self.merge_title = title

    def colum_drop(self, merge_df):
        return merge_df

    def nikei_merge(self):
        self.merge_ruiseki_df["日付"] =\
            self.merge_ruiseki_df["日付"].astype("datetime64[ns]")
        merge_df = pd.merge(
            self.merge_ruiseki_df, self.merge_nikei_data_df,
            on=["日付"], how='outer', indicator=True)
        merge_df = self.colum_drop(merge_df)
        # merge_df.to_csv(csv_path + '/tests/三菱自動車_link_マージ.csv')
        merge_df.to_csv(
            self.merge_path
            + self.merge_title
            + self.merge_file_name)
        return merge_df
