import re


class Niltukei_html:

    def get_html_title(self, driver):
        return re.search(r'【(.+)】', driver.title).group(1)
