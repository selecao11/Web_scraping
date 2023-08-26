import kabuka_select
import shinyou_zan
import gyakuhibu_taisyaku

class stock_related_select:

    '''
    def call_kabuka(title,WebDriverWait,driver,pd,By):
        ks = kabuka_select()
        kabu_df = ks(title,WebDriverWait,driver,pd,By)
        return kabu_df

    def call_shinyou_zan(title,WebDriverWait,driver,pd,By):
        sz = shinyou_zan()
        shinyou_df = sz(title,WebDriverWait,driver,pd,By)
        return shinyou_df

    def call_gyakuhibu_taisyaku(title,WebDriverWait,driver,pd,By):
        gt = gyakuhibu_taisyaku()
        gyakuhibu_taisyaku_df = gt(title,WebDriverWait,driver,pd,By)
        return gyakuhibu_taisyaku_df
    '''

    #逆日残を抽出
    def gyakuhibu_get(driver,title):
        gyakuhibu_taisyaku_df = srs.call_gyakuhibu_taisyaku(title,WebDriverWait,driver,pd,By)
        return gyakuhibu_taisyaku_df

    #信用残を抽出
    def shinyou_get(driver,title,kabu_df):
        shinyou_df =  ds.call_shinyou_zan(title,WebDriverWait,driver,pd,By)
        kabu_shinyou_data_df = pd.merge(kabu_df, shinyou_df, how="outer", on="日付")
        return kabu_shinyou_data_df

    #株価を抽出
    def kabu_get(company,driver,title):
        kabu_df =  ds.call_kabuka(title,WebDriverWait,driver,pd,By)
        return kabu_df
