from join import Join
import pandas as pd

def test_join_succes1():
    join_kabuka_df = pd.read_csv('/home/user/anaconda3/envs/web_scraping/source/test/三菱自動車_株価_.csv')
    join_shinyou_zan_df = pd.read_csv('/home/user/anaconda3/envs/web_scraping/source/test/三菱自動車_信用残_.csv')
    join_gyakuhibu_taisyaku_df = pd.read_csv('/home/user/anaconda3/envs/web_scraping/source/test/三菱自動車_逆日歩_貸借桟_.csv')

    jb = Join()
    jb.nikei_join_init(join_kabuka_df,join_shinyou_zan_df,join_gyakuhibu_taisyaku_df)
    nikei_join_df = jb.nikei_jion()
    nikei_join_df.to_csv('/home/user/anaconda3/envs/web_scraping/source/test/三菱自動車_株価_信用残_逆日歩_貸借桟.csv')
