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

    def updataRuikei(self, company_code, gyakuhibu_taisyaku_df):
        # 逆日歩貸借データフレームを参考に累積の累積貸株残で不一致の項目を更新する
        rc = Ruseki_control()
        gt = Gyakuhibu_taisyaku()
        ruiseki_df = rc.readRuiseki(Niltukei_const.CSV_PATH,
                                    gt.getGyakuhibuHtml(
                                        company_code,
                                        gt.newGyakuhibuDriver())
        )
        missmatch_koumoku = ["貸株残", "融資残", "貸株残", "逆日歩", "日歩日数"]
        data_frame = gyakuhibu_taisyaku_df
        for missmatch in missmatch_koumoku:
            ruiseki_df = rc.updataMismatchRuikei(missmatch,
                                                 ruiseki_df,
                                                 data_frame,
                                                 gyakuhibu_dict)

    def cleateGyakuhibuTaisyakuDf(self, company_code):
        gt = Gyakuhibu_taisyaku()
        file_name = Niltukei_const.FILE_NAME_GYAKUHIBU
        # gt.gyakuhibu_taisyaku_init_set(file_name, gyakuhibu_dict['csv_path'])
        h = Hizuke()
        dd = gt.getGyakuhibuHtml(company_code,
                                 gt.newGyakuhibuDriver())
        gyakuhibu_taisyaku_html = gt.searchGyakuhibuHtml(dd)
        # tableをDataFrameに格納
        gyakuhibu_df = gt.cleateGyakuhibuDf(gyakuhibu_taisyaku_html)
        gyakuhibu_taisyaku_df = gyakuhibu_df[0]
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

        # 逆日歩には差異があるので逆日歩貸借データフレームを参考に累積の累積貸株残で
        # 不一致の項目を更新する
        self.updataRuikei(company_code, gyakuhibu_taisyaku_df)

        nh = Niltukei_html()
        gyakuhibu_taisyaku_df.to_csv(gt.gyakuhibu_taisyaku_path
                                     + nh.getHtmlTitle(driver)
                                     + gt.gyakuhibu_taisyaku_file_name)
        return gyakuhibu_taisyaku_df
