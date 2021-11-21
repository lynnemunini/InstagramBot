from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import os
from selenium.webdriver.common.keys import Keys
s = Service("/home/lynne/Programs/Development/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://www.instagram.com/")
time.sleep(5)
# switch_accounts = driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/article/div[2]"
#                                                 "/div/div/div[3]/span/button")
# switch_accounts.click()
user_name = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
user_name.send_keys(os.environ["USER"])
password = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
password.send_keys(os.environ["PASSWORD"])
login = driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
login.click()
time.sleep(5)
not_now = driver.find_element(By.CSS_SELECTOR, "#react-root > section > main > div > div > div > div > button")
not_now.click()
time.sleep(5)
not_now_in = driver.find_element(By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC >"
                                                  " button.aOOlW.HoLwm")
not_now_in.click()
