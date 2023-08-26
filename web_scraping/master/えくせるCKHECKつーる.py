#pandasを読み込む
import pandas as pd
import re

#株データエクセルのPATHを設定
def master_ExcePath_set():
    master_Exce_path = '/home/user/anaconda3/envs/Web_scraping/株データ.xlsx'
    return master_Exce_path

#株データエクセルのエクセルオブジェクトの作成
def master_Book_get(master_Exce_path):
    master_book = pd.ExcelFile(master_Exce_path)
    return master_book

#株データエクセルオブジェクトから全てのシート名の取得
def master_names_sheet_get(master_book):
    master_names_sheet = master_book.sheet_names
    return master_names_sheet

#株データエクセルオブジェクトのシート数の取得
def master_num_Sheet_get(master_names_sheet):
    num_sheet = len(master_names_sheet)
    return num_sheet

#株データエクセルシートからデータフレームの生成
def master_Sheet_pd_get(master_book,sheet_name):
    master_sheet_df = master_book.parse(sheet_name)
    return master_sheet_df

def ruiseki_csv_read(ruiseki_sheet_name):
    print(ruiseki_sheet_name)
    ruiseki_csv_df = pd.read_csv('/home/user/anaconda3/envs/Web_scraping/累積株値data/'+ruiseki_sheet_name + '_累積.csv')
    return ruiseki_csv_df

def kabuka(master_sheet_df,ruiseki_csv_df):
    ruiseki_株価_csv_df = ruiseki_csv_df.loc[:,'日付':'修正後終値']
    print(ruiseki_株価_csv_df.head(10))

    master_sheet_df  = master_sheet_df.loc[:,'日付':'修正後終値']
    master_sheet_df['日付'] = master_sheet_df['日付'].replace('（.*', '',regex=True)
    master_sheet_df['日付'] = '2023/' + master_sheet_df['日付']
    print(master_sheet_df.head(10))

    # print(master_sheet_df.equals(ruiseki_株価_csv_df))
    master_sheet_df.to_csv('./コンペアdata/master_株価check.csv')
    ruiseki_株価_csv_df.to_csv('./コンペアdata/ruiseki_株価check.csv')

master_Exce_path = master_ExcePath_set()
master_book =  master_Book_get(master_Exce_path)
master_names_sheet = master_names_sheet_get(master_book)
num_sheet = master_num_Sheet_get(master_names_sheet)

'7211_三菱自動車'
del master_names_sheet
master_names_sheet=['7211_三菱自動車']

for sheet_name in master_names_sheet:
    master_sheet_df = master_Sheet_pd_get(master_book,sheet_name)
    sheet_name = re.sub(r'^[^_]*_', '', sheet_name)
    ruiseki_csv_df = ruiseki_csv_read(sheet_name)
    kabuka_dic = kabuka(master_sheet_df,ruiseki_csv_df)

"""#input file name
input_file_name = '/home/user/anaconda3/envs/Web_scraping/株データ.xlsx'
#xls book Open (xls, xlsxのどちらでも可能)
input_book = pd.ExcelFile(input_file_name)
#sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
master_sheet_names = input_book.sheet_names
#lenでシートの総数を確認
num_sheet = len(master_sheet_names)
#シートの数とシートの名前のリストの表示
print ("Sheet の数:", num_sheet)
print (master_sheet_names)

ruiseki_sheet_name = re.sub(r'^[^_]*_', '', master_sheet_names[0])
kabuka(master_sheet_names[0],ruiseki_sheet_name)


'''for sheet_name in input_sheet_name:
    print(sheet_name)
    input_sheet_df = input_book.parse(sheet_name)

    #読み込んだシート名の確認
    print("Sheet name:", input_sheet_name[0])
    #読み込んだシートの先頭10行を表示
    print(input_sheet_df.head(10))
    #株価データフレーム作成
    kabuka_df = pd.DataFrame(input_sheet_df.iloc[:,:7])
    kabuka_df.columns=['日付','始値','高値','安値','終値','売買高','修正後終値']
    #信用データフレーム作成
    shinyou_df = pd.DataFrame(input_sheet_df.iloc[:,7:11])
    shinyou_df.columns= ['日付','信用売残','信用買残','信用倍率']
    #逆日歩データフレーム作成
    gyakuhibu_taisyaku_df = pd.DataFrame(input_sheet_df.iloc[:,11:]) 
    gyakuhibu_taisyaku_df.columns =['日付','日証金','逆日歩','日歩日数','貸株残','融資残'] 

    #日付項目の曜日を削除
    kabuka_df['日付'] = kabuka_df['日付'].replace('（.*', '',regex=True)
    shinyou_df['日付'] = shinyou_df['日付'].replace('（.*', '',regex=True)
    gyakuhibu_taisyaku_df['日付'] = gyakuhibu_taisyaku_df['日付'].replace('（.*', '',regex=True)

    #日付項目の月日に年を追加
    kabuka_df['日付'] = '2023/' + kabuka_df['日付']
    gyakuhibu_taisyaku_df['日付'] = '2023/' + gyakuhibu_taisyaku_df['日付']

    #株価、信用、逆日歩データフレームのマージ
    kabu_shinyou_gyakuhibu_df = pd.merge(kabuka_df, shinyou_df, how="outer", on="日付")
    kabu_shinyou_gyakuhibu_taisyaku_df = pd.merge(kabu_shinyou_gyakuhibu_df, gyakuhibu_taisyaku_df, how="outer", on="日付")
    #日証金項目の削除
    kabu_shinyou_gyakuhibu_taisyaku_df = kabu_shinyou_gyakuhibu_taisyaku_df.drop('日証金', axis=1)
    kabu_shinyou_gyakuhibu_taisyaku_df =kabu_shinyou_gyakuhibu_taisyaku_df.fillna(0)
    print(kabu_shinyou_gyakuhibu_taisyaku_df.head(10))
    #ファイル出力
    sheet_name = re.sub(r'^[^_]*_', '', sheet_name)
    kabu_shinyou_gyakuhibu_taisyaku_df.to_csv('./累積株data/'+ sheet_name + '_累積_.csv')
"""
