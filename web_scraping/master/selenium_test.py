from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

#options = Options()
#options.add_argument('--headless')

options = webdriver.ChromeOptions()
options.add_argument('--headless')

# ダウンロード先のpath情報を指定
#executable_path = '/Users/myname/Downloads/chromedriver'
executable_path = '/home/user/anaconda3/envs/Web_scraping/chromedriver'

driver = webdriver.Chrome(executable_path, options=options)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")
title = driver.title
print(title)
