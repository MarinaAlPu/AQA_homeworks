import allure
from time import sleep
from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, browser):
        with allure.step("Открыть окно браузера"):
            self.browser = browser

        with allure.step("Перейти на страницу авторизации для входа в магазин\
                         по ссылке https://www.saucedemo.com/"):
            self.browser.get("https://www.saucedemo.com/")

        with allure.step("Подождать загрузки всех элементов на странице"):  
            self.browser.implicitly_wait(4)

        with allure.step("Развернуть окно браузера"):
            self.browser.maximize_window() 

    @allure.step("Ввести в поля ввода данные, необходимые для авторизации")
    def auth(self, user_name: str, password: str):
        with allure.step("В поле Username ввести имя пользователя"):
            self.browser.find_element(By.CSS_SELECTOR, '#user-name').send_keys(user_name)
        with allure.step("В поле Passwosd ввести пароль"):        
            self.browser.find_element(By.CSS_SELECTOR, '#password').send_keys(password)

    @allure.step("Нажать кнопку Login")
    def login(self) -> None:
        self.browser.find_element(By.CSS_SELECTOR, '#login-button').click()