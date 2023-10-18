import pandas as pd
from niltukei_const import Niltukei_const
file_name =["AGC_累積.csv",
    "JR西日本_累積.csv",
    "SUBARU_累積.csv",
    "みずほフィナンシャルグループ_累積.csv",
    "ゆうちょ銀行_累積.csv",
    "アドバンス・レジデンス投資法人_累積.csv",
    "スノーピーク_累積.csv",
    "チノー_累積.csv",
    "トヨタ自動車_累積.csv",
    "ハピネット_累積.csv",
    "パナソニックホールディングス_累積.csv",
    "ベルーナ_累積.csv",
    "ポプラ_累積.csv",
    "マツダ_累積.csv",
    "ヨコオ_累積.csv",
    "安川電機_累積.csv",
    "三菱自動車_累積.csv",
    "積水化学工業_累積.csv",
    "中越パルプ工業_累積.csv",
    "日本テレビホールディングス_累積.csv",
    "日本製鋼所_累積.csv",
    "野村不動産ホールディングス_累積.csv"]

for name in file_name:
    ruiseki_df = pd.read_csv(Niltukei_const.CSV_PATH + name,dtype={"日付":str})
    ruiseki_df["日付"] = pd.to_datetime(ruiseki_df["日付"], format="%Y-%m-%d")
    ruiseki_df["曜日"] = ruiseki_df["日付"].dt.weekday
    ruiseki_df.to_csv(Niltukei_const.CSV_PATH + '_曜日_' + name)
