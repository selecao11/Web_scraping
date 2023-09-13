import pandas as pd


class Test_pres():
    def readDataFrame(test_file_path, test_file_name):
        object_df = pd.read_csv(test_file_path + test_file_name, index_col=0)
        return object_df

    def readSeries(test_file_path, test_file_name):
        object_df = pd.read_csv(test_file_path + test_file_name, squeeze = True)
        return object_df
