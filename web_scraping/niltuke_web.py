from selenium import webdriver
from niltukei_const import Niltukei_const


class Niltukei_web:

    def cleate_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        executable_path = Niltukei_const.WEB_DRIVER\
            + Niltukei_const.WEB_CHROME_DRIVER
        driver = webdriver.Chrome(executable_path, options=options)
        driver.maximize_window()
        return driver
