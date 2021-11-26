import time
import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

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
        time.sleep(5)
        self.follow()

    def follow(self):
        activity = self.driver.find_element(By.CSS_SELECTOR, "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(5) > a > svg")
        activity.click()
        # time.sleep(5)
        # requests = self.driver.find_element(By.CSS_SELECTOR, "#react-root > section > nav > div._8MQSO.Cx7Bp > div > div > div.ctQZg.KtFt3 > div > div:nth-child(5) > div > div.uo5MA._2ciX.tWgj8.XWrBI > div._01UL2 > div > div > div > div.PUHRj.eKc9b.H_sJK > div.iTMfC > div > span > svg")
        # requests.click()
        time.sleep(5)
        try:
            requests_follow = self.driver.find_elements(By.XPATH, "//button[.='Confirm']")
        except NoSuchElementException:
            self.driver.close()
        else:
            for request in requests_follow:
                request.click()
                time.sleep(2)

            # follows = self.driver.find_elements(By.XPATH, "//button[.='Follow']")
            follows = self.driver.find_elements(By.CLASS_NAME, "iTMfC")
            # print(len(follows))
            for follow in follows:
                follow.click()
                time.sleep(2)



