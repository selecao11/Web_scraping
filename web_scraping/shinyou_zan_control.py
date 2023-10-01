# from hizuke import Hizuke
from shinyou_zan import Shinyou_zan
from niltukei_const import Niltukei_const


class Shinyou_zan_control:

    def cleateShinyouZanDf(self, shinyou_dict):
        sz = Shinyou_zan()
        file_name = Niltukei_const.FILE_NAME_SHINYOU
        sz.shinyou_zan_title_get(shinyou_dict['driver'])
        sz.shinyou_zan_init_set(file_name, shinyou_dict['csv_path'])
        shinyou_zan_html = sz.shinyou_zan_html_search(
            shinyou_dict['WebDriverWait'], shinyou_dict['driver'],
            shinyou_dict['By'])
        # tableをDataFrameに格納
        pd = shinyou_dict['pd']
        shinyou_zan_df = pd.read_html(shinyou_zan_html)
        shinyou_zan_df = shinyou_zan_df[0]
        # 信用桟データフレームのカラム名の変更
        shinyou_zan_df = sz.shinyou_zan_df_rename(shinyou_zan_df)
        shinyou_zan_df[Niltukei_const.HIZEKE_KOUMOKU] = pd.to_datetime(
            shinyou_zan_df[Niltukei_const.HIZEKE_KOUMOKU])
        # 取得したデータを記録
        shinyou_zan_df.to_csv(sz.shinyou_zan_path
                              + sz.shinyou_zan_sz_title
                              + sz.shinyou_zan_file_name)
        return shinyou_zan_df
