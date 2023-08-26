class shinyou_zan:

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
        shinyou_df.to_csv('./取得株値data/'+title+'_信用残_.csv')
        return shinyou_df   