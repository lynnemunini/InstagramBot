from login import LoginPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get('https://www.instagram.com/')

    def go_to_login_page(self):
        return LoginPage(self.driver)
