import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from task2.MainPage import MainPage

@allure.epic("Калькулятор")
@allure.suite("Работа калькулятора")
@allure.title("Проверка работы функций калькулятора")
@allure.description("Проверка корректности работы функции установки времени ожидания результата\
                    и получения корректного результата по истечении времени ожидания")
@allure.feature("Функция ожидания результата")
@allure.severity("Blocker")
@allure.id("Сalc-1")  
def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    main_page = MainPage(browser)

    main_page.delay("45")
    main_page.clear_entry_field()
    main_page.input_data()
    as_is = main_page.check_result()

    with allure.step("Проверить, что в поле ввода отображается результат: 15"):
        assert as_is == "15"

    with allure.step("Закрыть окно браузера"):
        browser.quit()