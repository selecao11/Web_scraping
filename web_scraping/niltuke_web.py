from selenium import webdriver
from niltukei_const import Niltukei_const
from niltukei_html import Niltukei_html

class Niltukei_web:

    def getTitle(self, driver):
        nh = Niltukei_html()
        return nh.getHtmlTitle(driver)

    def cleateDriver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        executable_path = Niltukei_const.WEB_DRIVER\
            + Niltukei_const.WEB_CHROME_DRIVER
        driver = webdriver.Chrome(executable_path, options=options)
        driver.maximize_window()
        return driver
