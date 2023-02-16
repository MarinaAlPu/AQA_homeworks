from task1.ClassUser import Users
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    def input_data(self):
        user = Users("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "123@test.ru", "+79123456789", "QA", "SkyPro")
        locators = ['input[name="first-name"]', 'input[name="last-name"]', 'input[name="address"]',
                'input[name="zip-code"]', 'input[name="city"]', 'input[name="country"]',
                'input[name="e-mail"]', 'input[name="phone"]', 'input[name="job-position"]', 'input[name="company"]']
        user_methods = [str(user.my_first_name()), str(user.my_last_name()), str(user.my_address()),
                        str(user.my_zip_code()), str(user.my_city()), str(user.my_country()),
                        str(user.my_email()), str(user.my_phone_number()), str(user.my_job_position()), str(user.my_company())]
        counter = 0
        for counter in range(0, 10):
            self.browser.find_element(By.CSS_SELECTOR, locators[counter]).send_keys(user_methods[counter])
            counter = counter + 1

    def click_button(self):
        self.browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').send_keys(Keys.ENTER)