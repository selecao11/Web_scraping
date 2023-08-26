class Hizuke:
    def year_add(self,hizuke_df):
        hizuke_df = '2023/' + hizuke_df
        return hizuke_df

    def day_of_week_delete(self,hizuke_df):
        hizuke_df = hizuke_df.replace('（.*', '',regex=True)
        return hizuke_df

