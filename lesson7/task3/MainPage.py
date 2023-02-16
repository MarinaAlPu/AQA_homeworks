from time import sleep
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/")
        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    def auth(self):#, user_name, password
        self.browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
        self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')

    def login(self):
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()