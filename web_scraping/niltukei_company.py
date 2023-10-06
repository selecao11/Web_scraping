
class Niltukei_company:

    def getCompanyHtml(self, company_code, driver):
        target_url = 'https://www.nikkei.com/nkd/company/?scode=' + company_code
        # driver = self.get_driver(target_url)
        driver.get(target_url)
        return driver
