import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, browser: str):
        with allure.step("Открыть окно браузера"):
            self.browser = browser

        with allure.step("Перейти на страницу с калькулятором\
                         по ссылке https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"):
            self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        with allure.step("Подождать загрузки всех элементов на странице"):  
            self.browser.implicitly_wait(4)
            
        with allure.step("Развернуть окно браузера"):
            self.browser.maximize_window() 

    @allure.step("Ввести время ожидания")
    def delay(self, time_for_delay: str):
        with allure.step("Очистить поле ввода времени ожидания"):
            self.browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        with allure.step("В поле ввода времени ожидания ввести значение 45"):
            self.browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(time_for_delay)

    @allure.step("Очистить поле отображения данных")
    def clear_entry_field(self) -> None:
        self.browser.find_element(By.XPATH, '//*[text()="C"]').click()    

    @allure.step("Нажать по очереди кнопки '7', '+', '8', '='")
    def input_data(self):
        locators = ['//*[text()="7"]', '//*[text()="+"]', '//*[text()="8"]', '//*[text()="="]']
        counter = 0
        for counter in range(0, 4):
            self.browser.find_element(By.XPATH, locators[counter]).click()
            counter = counter + 1
        with allure.step("Подождать 46 секунд, пока в поле отображения данных отобразится сумма"):    
            waiter = WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), "15") )

    @allure.step("Извлечь результат из поля отображения данных")
    def check_result(self) -> str:
        result = self.browser.find_element(By.CSS_SELECTOR, ('.screen')).text
        return result