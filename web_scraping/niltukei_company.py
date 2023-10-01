
class Niltukei_company:

    def getCompanyHtml(self, cmp, driver):
        target_url = 'https://www.nikkei.com/nkd/company/?scode=' + cmp
        # driver = self.get_driver(target_url)
        driver.get(target_url)
        return driver

