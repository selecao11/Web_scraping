import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.difference import Difference
import pandas as pd

csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"

def test_difference_succes1():
    merge_df = pd.read_csv(csv_path + '/tests/三菱自動車_マージ.csv')

    df = Difference()
    file_path = './'
    file_name = '_差分.csv'
    title = '三菱自動車'
    df.difference_init(merge_df,file_name,file_path,title)
    df.difference_select()
