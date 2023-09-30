import re


class Niltukei_html:

    def getHtmlTitle(self, driver):
        return re.search(r'【(.+)】', driver.title).group(1)
