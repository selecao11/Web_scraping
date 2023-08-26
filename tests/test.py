from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()

# 必要に応じてoptionsを設定
import pytest
driver = webdriver.Chrome()
print('okok')
# driverからウェブブラウザの操作を実行

driver.quit()
