from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver

class chrome_driver:

    #chromedriverをセット
    @staticmethod
    def chrome_driver_set():
        chrome_driver = webdriver.Chrome('./chromedriver')
        chrome_driver.maximize_window()
        return chrome_driver
