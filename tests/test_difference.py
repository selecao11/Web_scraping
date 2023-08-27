import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.Difference import Difference
import pandas as pd

csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"

def test_difference_succes1():
    merge_df = pd.read_csv(csv_path + '/tests/三菱自動車_マージ.csv')

    df = Difference()
    df.difference_init(merge_df)
    difference_d = df.difference_select()
    difference_d.to_csv(csv_path + '/tests/三菱自動車_差分.csv')
