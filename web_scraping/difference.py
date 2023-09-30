from niltukei_const import Niltukei_const


class Difference:

    merge_df = None
    difference_df = None

    difference_path = None
    difference_file_name = None
    difference_title = None

    def difference_init(self, merge_df, file_name, file_path, title):
        self.merge_df = merge_df
        self.difference_path = file_path
        self.difference_file_name = file_name
        self.difference_title = title

    def dropColum(self, niltukei_join_df):
        difference_df = niltukei_join_df
        # Unnamed: 0
        '''
        self.difference_df = self.difference_df.drop\
            (Niltukei_const.STOCK_PRICE_ACCUMULATION_UNNAMED_0_KOUMOKU, axis=1)
        '''
        # 累積始値
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_HAJIMARINE_KOUMOKU, axis=1)

        # 累積高値
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_TAKENE_KOUMOKU, axis=1)

        # 累積安値
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_YASUNE_KOUMOKU, axis=1)

        # 累積終値
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_OWARINE_KOUMOKU, axis=1)

        # 累積売買高
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_URIKAIDAKA_KOUMOKU, axis=1)

        # 累積修正後終値
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_SYUSEIGO_OWARINE_KOUMOKU, axis=1)

        # 累積信用売残
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_SHINYOU_URI_KOUMOKU, axis=1)

        # 累積信用買残
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_SHINYOU_KAI_KOUMOKU, axis=1)

        # 累積信用倍率
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_SHINYOU_BAI_KOUMOKU, axis=1)

        # 累積逆日歩
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_GYAKUHIBU_KOUMOKU, axis=1)

        # 累積日歩日数
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_HIBU_KOUMOKU, axis=1)

        # 累積貸株残
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_KASHIKABU_ZAN, axis=1)

        # 累積融資残
        difference_df = difference_df.drop(
            Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU, axis=1)

        # _merge
        difference_df = difference_df.drop(
            Niltukei_const.MERGE_KOUMOKU, axis=1)
        return difference_df

    def renameColum(self, niltukei_join_df):
        difference_df = niltukei_join_df
        return difference_df.rename(columns={
            Niltukei_const.HAJIMARINE_KOUMOKU:
            Niltukei_const.RUISEKI_HAJIMARINE_KOUMOKU,
            Niltukei_const.TAKENE_KOUMOKU:
            Niltukei_const.RUISEKI_TAKENE_KOUMOKU,
            Niltukei_const.YASUNE_KOUMOKU:
            Niltukei_const.RUISEKI_YASUNE_KOUMOKU,
            Niltukei_const.OWARINE_KOUMOKU:
            Niltukei_const.RUISEKI_OWARINE_KOUMOKU,
            Niltukei_const.URIKAIDAKA_KOUMOKU:
            Niltukei_const.RUISEKI_URIKAIDAKA_KOUMOKU,
            Niltukei_const.SYUSEIGO_OWARINE_KOUMOKU:
            Niltukei_const.RUISEKI_SYUSEIGO_OWARINE_KOUMOKU,
            Niltukei_const.SHINYOU_URI_KOUMOKU:
            Niltukei_const.RUISEKI_SHINYOU_URI_KOUMOKU,
            Niltukei_const.SHINYOU_KAI_KOUMOKU:
            Niltukei_const.RUISEKI_SHINYOU_KAI_KOUMOKU,
            Niltukei_const.SHINYOU_BAI_KOUMOKU:
            Niltukei_const.RUISEKI_SHINYOU_BAI_KOUMOKU,
            Niltukei_const.GYAKUHIBU_KOUMOKU:
            Niltukei_const.RUISEKI_GYAKUHIBU_KOUMOKU,
            Niltukei_const.HIBU_KOUMOKU:
            Niltukei_const.RUISEKI_HIBU_KOUMOKU,
            Niltukei_const.KASHIKABU_ZAN:
            Niltukei_const.RUISEKI_KASHIKABU_ZAN,
            Niltukei_const.YUSHI_ZAN_KOUMOKU:
            Niltukei_const.RUISEKI_YUSHI_ZAN_KOUMOKU})

