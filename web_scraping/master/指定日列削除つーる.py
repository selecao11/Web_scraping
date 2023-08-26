#pandasを読み込む
import pandas as pd
import glob
import os

#input file name
#input_file_name = '株データ.xlsx'
files = glob.glob("/home/user/anaconda3/envs/Web_scraping/累積株値data/累積_old/*")
for input_file_name in files:
#xls book Open (xls, xlsxのどちらでも可能)
    #input_book = pd.ExcelFile(input_file_name)
    input_book_df = pd.read_csv(input_file_name,index_col=1)
    input_book_df = input_book_df.drop('Unnamed: 0', axis=1)
    print(input_book_df)
    input_book_df = input_book_df.drop('2023-07-21')
    file_name = os.path.split(input_file_name)[1]
    input_book_df.to_csv('/home/user/anaconda3/envs/Web_scraping/累積株値data/'+ file_name )
