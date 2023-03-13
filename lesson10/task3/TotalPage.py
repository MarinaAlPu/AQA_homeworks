import allure
from time import sleep
from selenium.webdriver.common.by import By

class TotalPage:
    def __init__(self, browser):
        self.browser = browser

        with allure.step("Открылась страница оформления заказа"): 
            self.browser.get("https://www.saucedemo.com/checkout-step-two.html")

        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    @allure.step("Извлечь из поля Total общую сумму заказа")
    def get_total(self) -> str:
        txt = self.browser.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
        return txt