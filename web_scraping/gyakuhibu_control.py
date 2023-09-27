from hizuke import Hizuke
from gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from niltukei_const import Niltukei_const


class Gyakuhibu_control:

    def cleate_gyakuhibu_taisyaku_df(self, Gyakuhibu_dict):
        gt = Gyakuhibu_taisyaku()
        file_name = Niltukei_const.FILE_NAME_GYAKUHIBU
        gt.gyakuhibu_taisyaku_title_get(Gyakuhibu_dict['driver'])
        gt.gyakuhibu_taisyaku_init_set(file_name, Gyakuhibu_dict['csv_path'])
        h = Hizuke()
        gyakuhibu_taisyaku_html = gt.gyakuhibu_taisyaku_html_search(
            Gyakuhibu_dict['WebDriverWait'], Gyakuhibu_dict['driver'],
            Gyakuhibu_dict['By'])
        # tableをDataFrameに格納
        pd = Gyakuhibu_dict['pd']
        gyakuhibu_taisyaku_df = pd.read_html(gyakuhibu_taisyaku_html)
        gyakuhibu_taisyaku_df = gyakuhibu_taisyaku_df[0]
        # 逆日歩貸借データフレームのカラム名の変更
        gyakuhibu_taisyaku_df = gt.gyakuhibu_taisyaku_df_rename(
            gyakuhibu_taisyaku_df)
        # 逆日歩貸借データフレームのカラム名の変更
        hizuke_df = gyakuhibu_taisyaku_df[gt.hizuke_koumoku]
        # 逆日歩貸借データフレームの日付項目の曜日を削除
        hizuke_df = gt.gyakuhibu_taisyaku_youbi_del(
            gyakuhibu_taisyaku_df, h, hizuke_df)
        # 逆日歩貸借データフレームの日付項目の月日に年を追加
        gyakuhibu_taisyaku_df = gt.gyakuhibu_taisyaku_hizuke_yy_add(
            gyakuhibu_taisyaku_df, h, hizuke_df)
        # 逆日歩貸借データフレームの項目削除、置換
        gyakuhibu_taisyaku_df = gt.gyakuhibu_taisyaku_item_replace(
            gyakuhibu_taisyaku_df)
        gyakuhibu_taisyaku_df = gt.gyakuhibu_taisyaku_item_drop(
            gyakuhibu_taisyaku_df)

        gyakuhibu_taisyaku_df.to_csv(gt.gyakuhibu_taisyaku_path
                                     + gt.gyakuhibu_taisyaku_title
                                     + gt.gyakuhibu_taisyaku_file_name)
        return gyakuhibu_taisyaku_df
