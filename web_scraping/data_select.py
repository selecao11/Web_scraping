def year_add(hizuke_df):
    hizuke_df = '2023/' + hizuke_df
    return hizuke_df

def day_of_week_delete(hizuke_df):
    hizuke_df = hizuke_df.replace('（.*', '',regex=True)
    return hizuke_df

def kabuka(title,WebDriverWait,driver,pd,By):
    kabuka = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.LINK_TEXT, "株価"))
    print(kabuka.get_attribute("href"))
    kabuka.click()
    kabuka_table = WebDriverWait(driver, 10).until(lambda y: y.find_element(By.CLASS_NAME, "w668"))
    kabuka_html=kabuka_table.get_attribute("outerHTML") #table要素を含むhtmlを取得
    kabuka_df=pd.read_html(kabuka_html) #tableをDataFrameに格納
    kabu_df = kabuka_df[0]
    kabu_df = kabu_df.rename(columns={'日付':'日付','始値':'始値','高値':'高値','安値':'安値','終値':'終値',\
                                       '売買高':'売買高','修正後終値':'修正後終値'})
    #kabu_df = pd.DataFrame(kabu_df)
    print(type(kabu_df))
    print(kabu_df)
    #日付項目の曜日を削除
    hizuke_df = kabu_df['日付']
    hizuke_df = day_of_week_delete(hizuke_df)
    #日付項目の月日に年を追加
    hizuke_df = year_add(hizuke_df)
    kabu_df['日付'] = hizuke_df
    kabu_df["日付"] = pd.to_datetime(kabu_df["日付"])
    print(kabu_df)
    #取得したデータを記録 Acquisition_share_value_data
    kabu_df.to_csv('/home/user/anaconda3/envs/web_scraping/source/Acquisition_share_value_data/'+title+'_株価_.csv')
    return kabu_df

def shinyou_zan(title,WebDriverWait,driver,pd,By):
    shinyou_zan = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.LINK_TEXT, "信用残"))
    #print(shinyou_zan.get_attribute("href"))
    shinyou_zan.click()
    shinyou_table = WebDriverWait(driver, 10).until(lambda y: y.find_element(By.CLASS_NAME, "w668"))
    shinyou_html=shinyou_table.get_attribute("outerHTML") #table要素を含むhtmlを取得
    shinyou_df=pd.read_html(shinyou_html) #tableをDataFrameに格納
    shinyou_df = shinyou_df[0]
    #print(shinyou_df)
    shinyou_df = shinyou_df.rename(columns={'日付':'日付',\
                                            '信用売残 （解説）':'信用売残',\
                                            '信用買残 （解説）':'信用買残',\
                                            '信用倍率 （解説）':'信用倍率'})
    shinyou_df["日付"] = pd.to_datetime(shinyou_df["日付"])
    print(shinyou_df)
    #取得したデータを記録
    shinyou_df.to_csv('/home/user/anaconda3/envs/web_scraping/source/Acquisition_share_value_data/'+title+'_信用残_.csv')
    return shinyou_df

def gyakuhibu_taisyaku(title,WebDriverWait,driver,pd,By):
    gyakuhibu_taisyaku = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.LINK_TEXT, "逆日歩・貸借残"))
    #逆日歩をクリック
    gyakuhibu_taisyaku.click()
    gyakuhibu_taisyaku_table = WebDriverWait(driver, 10).until(lambda y: y.find_element(By.CLASS_NAME, "w668"))
    gyakuhibu_taisyaku_html=gyakuhibu_taisyaku_table.get_attribute("outerHTML") #table要素を含むhtmlを取得
    gyakuhibu_taisyaku_df=pd.read_html(gyakuhibu_taisyaku_html) #tableをDataFrameに格納
    print(gyakuhibu_taisyaku_df)
    gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df[0]
    #日付項目の曜日を削除
    hizuke_df = gyakuhibu_taisyaku_df['日付']
    hizuke_df = day_of_week_delete(hizuke_df)
    #日付項目の月日に年を追加
    hizuke_df = year_add(hizuke_df)
    gyakuhibu_taisyaku_df['日付'] = hizuke_df
    print(gyakuhibu_taisyaku_df)
    gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df.rename(columns={'日付':'日付',\
                                            'Unnamed: 1':'日証金',\
                                            '逆日歩（円）':'逆日歩',\
                                            '日歩日数（日）':'日歩日数',\
                                            '貸株残（株）':'貸株残',\
                                            '融資残（株）':'融資残'
                                            })
    gyakuhibu_taisyaku_df["日付"] = pd.to_datetime(gyakuhibu_taisyaku_df["日付"])
    print(gyakuhibu_taisyaku_df)
    #取得したデータを記録
    gyakuhibu_taisyaku_df.to_csv('/home/user/anaconda3/envs/web_scraping/source/Acquisition_share_value_data/'+title+'_逆日歩_貸借桟_.csv')
    return gyakuhibu_taisyaku_df



def call_kabuka(title,WebDriverWait,driver,pd,By):
    kabu_df = kabuka(title,WebDriverWait,driver,pd,By)
    return kabu_df

def call_shinyou_zan(title,WebDriverWait,driver,pd,By):
    shinyou_df = shinyou_zan(title,WebDriverWait,driver,pd,By)
    return shinyou_df

def call_gyakuhibu_taisyaku(title,WebDriverWait,driver,pd,By):
    gyakuhibu_taisyaku_df = gyakuhibu_taisyaku(title,WebDriverWait,driver,pd,By)
    return gyakuhibu_taisyaku_df

