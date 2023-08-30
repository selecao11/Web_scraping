import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.merge import Merge
import pandas as pd

csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"

def test_merge_succes1():
    ruiseki_df = pd.read_csv(csv_path + '/tests/三菱自動車_累積.csv')
    nikei_data_df = pd.read_csv(csv_path + '/tests/三菱自動車_株価_信用残_逆日歩_貸借桟.csv')

    mg = Merge()
    file_path = './'
    file_name = '_マージ.csv'
    title = '三菱自動車'

    mg.nikei_merge_init(ruiseki_df,nikei_data_df,file_path,file_name,title)
    merge_df = mg.nikei_merge()
    #merge_df.to_csv(csv_path + '/tests/三菱自動車_マージ.csv')
