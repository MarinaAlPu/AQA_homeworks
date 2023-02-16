from time import sleep
from selenium.webdriver.common.by import By

class TotalPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.saucedemo.com/checkout-step-two.html")
        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    def get_total(self):
        txt = self.browser.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return txt