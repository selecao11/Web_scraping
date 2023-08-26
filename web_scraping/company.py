import re

class Company:

    #抽出対象会社をセット
    def company_no_set(self):
        companys_no = ['7211','3231','7601','6850','7552','3269','6752','7182','8411','3877','7270','9021','7816','7203','5201','9997',
        '9404','6800','4204','6506','7261']
        #company = ['7211']
        return companys_no

    def company_html_get(self,chrome_driver,cmp):
        target_url = 'https://www.nikkei.com/nkd/company/?scode='+ cmp
    #    soup = BeautifulSoup(target_url,'html.parser')
        chrome_driver.get(target_url)
        comp_html = chrome_driver
        return comp_html

    def company_title_get(self,chrome_driver,cmp):
        comp_html = self.html_get(chrome_driver,cmp)
        title_val = re.search(r'【(.+)】',comp_html.title).group(1)
        return title_val 

