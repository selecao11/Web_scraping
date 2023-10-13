from hizuke import Hizuke
from gyakuhibu_taisyaku import Gyakuhibu_taisyaku
from niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html
from ruiseki_control import Ruseki_control
import config
from ruseki_mismatch import RuisekiMismatch


class Gyakuhibu_control:

    """     # ページタイトル取得
        def getGyakuhibuHtmlTitle(self, driver):
            gt = Gyakuhibu_taisyaku()
            return gt.getGyakuhibuTitle(driver)
    """
    def updataRuikei(self, company_code,
                     gyakuhibu_driver,
                     gyakuhibu_taisyaku_df):
        # 逆日歩貸借データフレームを参考に累積の累積貸株残で不一致の項目を更新する
        rc = Ruseki_control()
        rm = RuisekiMismatch()
        ruiseki_df = rc.readRuiseki()
        missmatch_koumoku = ["貸株残", "融資残", "貸株残", "逆日歩", "日歩日数"]
        data_frame = gyakuhibu_taisyaku_df
        for missmatch in missmatch_koumoku:
            ruiseki_df = rc.updataMismatchRuikei(company_code,
                                                 gyakuhibu_driver,
                                                 missmatch,
                                                 ruiseki_df,
                                                 data_frame)
        rm.saveMismatchRuseki(rm.dropRuseki(ruiseki_df))

    def cleateGyakuhibuTaisyakuDf(self, company_code):
        gt = Gyakuhibu_taisyaku()
        h = Hizuke()
        gyakuhibu_driver = gt.getGyakuhibuHtml(company_code,
                                               gt.newGyakuhibuDriver())
        gyakuhibu_taisyaku_html = gt.searchGyakuhibuHtml(gyakuhibu_driver)
        # 使用済のドライバの開放
        gt.delGyakuhibuDriver(gyakuhibu_driver)
        # tableをDataFrameに格納
        gyakuhibu_df = gt.cleateGyakuhibuDf(gyakuhibu_taisyaku_html)
        gyakuhibu_taisyaku_df = gyakuhibu_df[0]
        # 逆日歩貸借データフレームのカラム名の変更
        gyakuhibu_taisyaku_df = gt.renameGyakuhibuDf(
            gyakuhibu_taisyaku_df)
        # 逆日歩貸借データフレームのカラム名の変更
        hizuke_df = gyakuhibu_taisyaku_df[gt.hizuke_koumoku]
        # 逆日歩貸借データフレームの日付項目の曜日を削除
        hizuke_df = gt.delGyakuhibuDayOfWeek(
            gyakuhibu_taisyaku_df, h, hizuke_df)
        # 逆日歩貸借データフレームの日付項目の月日に年を追加
        gyakuhibu_taisyaku_df = gt.addGyakuhibuYear(
            gyakuhibu_taisyaku_df, h, hizuke_df)
        # 逆日歩貸借データフレームの項目削除、置換
        gyakuhibu_taisyaku_df = gt.replaceZeroGyakuhibuItem(
            gyakuhibu_taisyaku_df)
        gyakuhibu_taisyaku_df = gt.dropGyakuhibuItem(
            gyakuhibu_taisyaku_df)

        # 逆日歩には差異があるので逆日歩貸借データフレームを参考に累積の累積貸株残で
        # 不一致の項目を更新する
        self.updataRuikei(company_code,
                          gyakuhibu_driver,
                          gyakuhibu_taisyaku_df)

        gyakuhibu_taisyaku_df.to_csv(Niltukei_const.CSV_PATH
                                     + config.title
                                     + Niltukei_const.FILE_NAME_GYAKUHIBU)
        return gyakuhibu_taisyaku_df
