import allure
from task1.ClassUser import Users
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage:
    def __init__(self, browser):
        with allure.step("Открыть окно браузера"):
            self.browser = browser

        with allure.step("Перейти на страницу с формой ввода данных\
                         по ссылке https://bonigarcia.dev/selenium-webdriver-java/data-types.html"):
            self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        with allure.step("Подождать загрузки всех элементов на странице"):  
            self.browser.implicitly_wait(4)

        with allure.step("Развернуть окно браузера"):
            self.browser.maximize_window() 

    @allure.step("Заполнить поля формы данными пользователя")
    def input_data(self) -> None:
        with allure.step("Создать экземпляр класса User"):
            user = Users("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "123@test.ru", "+79123456789", "QA", "SkyPro")
            locators = ['input[name="first-name"]', 'input[name="last-name"]', 'input[name="address"]',
                    'input[name="zip-code"]', 'input[name="city"]', 'input[name="country"]',
                    'input[name="e-mail"]', 'input[name="phone"]', 'input[name="job-position"]', 'input[name="company"]']
            user_methods = [str(user.my_first_name()), str(user.my_last_name()), str(user.my_address()),
                            str(user.my_zip_code()), str(user.my_city()), str(user.my_country()),
                            str(user.my_email()), str(user.my_phone_number()), str(user.my_job_position()), str(user.my_company())]
        
        with allure.step("Внести данные пользователя в соответствующие поля формы"):
            counter = 0
            for counter in range(0, 10):
                self.browser.find_element(By.CSS_SELECTOR, locators[counter]).send_keys(user_methods[counter])
                counter = counter + 1

    @allure.step("Нажать кнопку Submit")
    def click_button(self) -> None:
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').send_keys(Keys.ENTER)