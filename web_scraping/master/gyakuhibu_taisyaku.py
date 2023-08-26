class gyakuhibu_taisyaku:

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
        gyakuhibu_taisyaku_df.to_csv('./取得株値data/'+title+'_逆日歩_貸借桟_.csv')
        return gyakuhibu_taisyaku_df