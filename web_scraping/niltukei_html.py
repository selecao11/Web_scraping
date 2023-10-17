import re


class Niltukei_html:

    def getHtmlTitle(self, driver):
        """ 日経のページからページタイトルの取得

        Args:
            driver (webdriver): 日経のHTMLページ

        Returns:
            String: ページタイトル
        """
        return re.search(r'【(.+)】', driver.title).group(1)
