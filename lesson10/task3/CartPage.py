import allure
from time import sleep
from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, browser):
        self.browser = browser

        with allure.step("Открылась корзина"):  
            self.browser.get("https://www.saucedemo.com/cart.html")

        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    @allure.step("Нажать кнопку Checkout")
    def checkout(self):
        self.browser.find_element(By.CSS_SELECTOR, '#checkout').click()