#pandasを読み込む
import pandas as pd
import re

#input file name
input_file_name = '/home/user/anaconda3/envs/Web_scraping/master株data/株データ.xlsx'
#xls book Open (xls, xlsxのどちらでも可能)
input_book = pd.ExcelFile(input_file_name)
#sheet_namesメソッドでExcelブック内の各シートの名前をリストで取得できる
input_sheet_name = input_book.sheet_names
#lenでシートの総数を確認
num_sheet = len(input_sheet_name)
#シートの数とシートの名前のリストの表示
print ("Sheet の数:", num_sheet)
print (input_sheet_name)

del input_sheet_name
input_sheet_name=['7211_三菱自動車']

for sheet_name in input_sheet_name:
    print(sheet_name)
    input_sheet_df = input_book.parse(sheet_name)

    #読み込んだシート名の確認
    print("Sheet name:", input_sheet_name[0])
    #読み込んだシートの先頭10行を表示
    #print(input_sheet_df.head(10))
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
    #日付項目がNaNの行を削除
    kabu_shinyou_gyakuhibu_taisyaku_df = kabu_shinyou_gyakuhibu_taisyaku_df.dropna(subset=['日付'])
    print(kabu_shinyou_gyakuhibu_taisyaku_df.tail(10))
    #NaNの値を0に変換
    kabu_shinyou_gyakuhibu_taisyaku_df =kabu_shinyou_gyakuhibu_taisyaku_df.fillna(0)
    #シート名の企業コード削除
    sheet_name = re.sub(r'^[^_]*_', '', sheet_name)
    #ファイル出力
    #sheet_name.rename(columns={'A': 'Col_1'})
    kabu_shinyou_gyakuhibu_taisyaku_df.to_csv('./累積株値data/'+ sheet_name + '_累積.csv')

