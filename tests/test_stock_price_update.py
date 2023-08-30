import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from  web_scraping.niltukei_const import Niltukei_const
import pandas as pd
#csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"
csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/Cumulative_stock_price_data/"
new_csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/web_scraping/Cumulative_stock_price_data_new/"
def stock_price_item_replace(stock_price_df):
    stock_price_df = stock_price_df.replace({'累積逆日歩': {'-': 0}})
    stock_price_df = stock_price_df.replace({'累積日歩日数': {'-': 0}})
    return stock_price_df

def test_stock_price_update_succes1():
    import glob
    stock_price_df = None

    files = glob.glob(csv_path +"/*累積*")
    for file in files:
        stock_price_df = pd.read_csv(file)
        stock_price_df = stock_price_item_replace(stock_price_df)
        stock_price_df = stock_price_df.drop(\
            Niltukei_const.STOCK_PRICE_ACCUMULATION_UNNAMED_0_KOUMOKU, axis=1)
        file_name = os.path.basename(file)
        stock_price_df.to_csv(new_csv_path + file_name)
    #return stock_price_df

test_stock_price_update_succes1()



