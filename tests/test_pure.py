import pandas as pd
import pytest


class Test_pres():
    def data_read(test_file_path, test_file_name):
        object_df = pd.read_csv(test_file_path + test_file_name, index_col=0)
        return object_df
