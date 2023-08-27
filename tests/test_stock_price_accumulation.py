import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.stock_price_accumulation import StockPriceAccumulation
import pandas as pd

csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"

def test_join_succes1():
    stock_price_accumulation_df = pd.read_csv(csv_path +'tests/三菱自動車_累積.csv')
    difference_df = pd.read_csv(csv_path +'tests/三菱自動車_差分.csv')


    spa = StockPriceAccumulation()
    spa.stock_price_accumulation_init(difference_df,stock_price_accumulation_df)
    accumulation_df =  spa.stock_price_accumulation()
    accumulation_df.to_csv(csv_path + 'tests/test_三菱自動車_累積.csv')
