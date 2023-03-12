import allure
from time import sleep
from selenium.webdriver.common.by import By

class ShopPage:
    def __init__(self, browser):
        self.browser = browser

    @allure.step("Добавить в корзину следующие товары:")
    def add_product(self):
        with allure.step("Sauce Labs Backpack"):
            self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()

        with allure.step("Sauce Labs Bolt T-Shirt"):
            self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()

        with allure.step("Sauce Labs Onesie"):        
            self.browser.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()   