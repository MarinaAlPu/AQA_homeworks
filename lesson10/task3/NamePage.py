import allure
from time import sleep
from selenium.webdriver.common.by import By

class NamePage:
    def __init__(self, browser):
        self.browser = browser
        with allure.step("Открылась страница ввода персональных данных"):        
            self.browser.get("https://www.saucedemo.com/checkout-step-one.html")

        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    @allure.step("Ввести в поля ввода следующие персональные данные пользователя:")
    def personal_data(self, first_name: str, last_name: str, postal_code: int) -> None:
        with allure.step("В поле 'First Name' ввести имя пользователя"):
            self.browser.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)

        with allure.step("В поле 'Last Name' ввести фамилию пользователя"):
            self.browser.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)

        with allure.step("В поле 'Zip/Postal Code' ввести почтовый индекс пользователя"):
            self.browser.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
