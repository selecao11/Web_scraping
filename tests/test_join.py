import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))

from web_scraping.join import Join
import pandas as pd
csv_path = "/home/user/anaconda3/envs/web_scraping/web_scraping/"

def test_join_succes1():
    join_kabuka_df = pd.read_csv(csv_path +'tests/三菱自動車_株価_.csv')
    join_shinyou_zan_df = pd.read_csv(csv_path + 'tests/三菱自動車_信用残_.csv')
    join_gyakuhibu_taisyaku_df = pd.read_csv(csv_path + 'tests/三菱自動車_逆日歩_貸借桟_.csv')

    jb = Join()
    jb.nikei_join_init(join_kabuka_df,join_shinyou_zan_df,join_gyakuhibu_taisyaku_df)
    nikei_join_df = jb.nikei_jion()
    nikei_join_df.to_csv(csv_path + 'tests/三菱自動車_株価_信用残_逆日歩_貸借桟.csv')
