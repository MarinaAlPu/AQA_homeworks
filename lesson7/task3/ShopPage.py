from time import sleep
from selenium.webdriver.common.by import By

class ShopPage:
    def __init__(self, browser):
        self.browser = browser

    def add_product(self):
        self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
        self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
        self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()   