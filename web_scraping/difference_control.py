
class Difference_control:

    def select_difference(self):
        self.difference_df = self.merge_df[self.merge_df["_merge"] ==
                                           "right_only"]
        print(self.difference_df)
        self.colum_drop()
        self.colum_rename()
        self.difference_df.to_csv(self.difference_path + self.difference_title
                                  + self.difference_file_name)
        return self.difference_df
