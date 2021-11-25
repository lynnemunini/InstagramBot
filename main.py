from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from homepage import HomePage
import os
s = Service("/home/lynne/Programs/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(5)

home_page = HomePage(driver)
login_page = home_page.go_to_login_page()
login_page.login(os.environ["USER"], os.environ["PASSWORD"])

# driver.close()
