import pandas as pd


class Test_pres():

    def test_data_read(test_file_path, test_file_name):
        object_df = pd.read_csv(test_file_path + test_file_name)
        return object_df
