import time
import os

from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        user_name = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(1) > div > label > input")
        user_name.send_keys(os.environ["USER"])
        password = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(2) > div > label > input")
        password.send_keys(os.environ["PASSWORD"])
        login = self.driver.find_element(By.CSS_SELECTOR, "#loginForm > div > div:nth-child(3) > button")
        login.click()
        time.sleep(5)
        not_now = self.driver.find_element(By.CSS_SELECTOR, "#react-root > section > main > div > div > div > div > button")
        not_now.click()
        time.sleep(5)
        not_now_in = self.driver.find_element(By.CSS_SELECTOR, "body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC >"
                                                          " button.aOOlW.HoLwm")
        not_now_in.click()
