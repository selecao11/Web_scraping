import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.merge import Merge
import pandas as pd

def test_merge_succes1():
    ruiseki_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/source/test/三菱自動車_累積.csv')
    nikei_data_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/source/test/三菱自動車_株価_信用残_逆日歩_貸借桟.csv')

    mg = Merge()
    mg.nikei_merge_init(ruiseki_df,nikei_data_df)
    merge_df = mg.nikei_merge()
    merge_df.to_csv('/home/user/anaconda3/envs/Web_scraping/source/test/三菱自動車_マージ.csv')
