from time import sleep
from selenium.webdriver.common.by import By

class NamePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/checkout-step-one.html")
        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    def personal_data(self):
        self.browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Marina")
        self.browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Pudovkina")
        self.browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")