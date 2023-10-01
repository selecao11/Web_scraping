from hizuke import Hizuke
from gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html
from ruiseki_control import Ruseki_control


class Gyakuhibu_control:

    # ページタイトル取得
    def getGyakuhibuHtmlTitle(self, driver):
        gt = Gyakuhibu_taisyaku()
        return gt.getGyakuhibuTitle(driver)

    def updataRuikei(self, gyakuhibu_dict, gyakuhibu_taisyaku_df, driver):
        # 逆日歩貸借データフレームを参考に累積の累積貸株残で不一致の項目を更新する
        rc = Ruseki_control()
        ruiseki_df = rc.readRuiseki(gyakuhibu_dict['csv_path'], driver)
        return rc.updataStockLendingMismatch(ruiseki_df, gyakuhibu_taisyaku_df)

    def cleateGyakuhibuTaisyakuDf(self, gyakuhibu_dict, driver):
        gt = Gyakuhibu_taisyaku()
        file_name = Niltukei_const.FILE_NAME_GYAKUHIBU
        gt.gyakuhibu_taisyaku_init_set(file_name, gyakuhibu_dict['csv_path'])
        h = Hizuke()
        gyakuhibu_taisyaku_html = gt.gyakuhibu_taisyaku_html_search(
            gyakuhibu_dict['WebDriverWait'], gyakuhibu_dict['driver'],
            gyakuhibu_dict['By'])
        # tableをDataFrameに格納
        pd = gyakuhibu_dict['pd']
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

        self.updataRuikei(gyakuhibu_dict, gyakuhibu_taisyaku_df, driver)

        nh = Niltukei_html()
        gyakuhibu_taisyaku_df.to_csv(gt.gyakuhibu_taisyaku_path
                                     + nh.getHtmlTitle(driver)
                                     + gt.gyakuhibu_taisyaku_file_name)
        return gyakuhibu_taisyaku_df
