import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from task1.MainPage import MainPage
from task1.UserPage import UserPage

@allure.epic("Форма ввода данных")
@allure.suite("Заполнение формы ввода данных")
@allure.title("Проверка цвета поля")
@allure.description("Проверка корректности окрашивания полей в зависимости от наличия в них данных")
@allure.feature("Окрашивание полей")
@allure.severity("Normal")
@allure.id("UF-1")  
def test_user_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        
    main_page = MainPage(browser)
        
    main_page.input_data()
    main_page.click_button()
        
    user_page = UserPage(browser)

    green = "rgba(209, 231, 221, 1)"
    red = "rgba(248, 215, 218, 1)"

    clr1 = user_page.get_color1()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr1 == green

    clr2 = user_page.get_color2()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr2 == green

    clr3 = user_page.get_color3()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr3 == green

    clr4 = user_page.get_color4()
    with allure.step("Проверить, что поле красного цвета"):
        assert clr4 == red

    clr5 = user_page.get_color5()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr5 == green

    clr6 = user_page.get_color6()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr6 == green

    clr7 = user_page.get_color7()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr7 == green

    clr8 = user_page.get_color8()
    assert clr8 == green

    clr9 = user_page.get_color9()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr9 == green

    clr10 = user_page.get_color10()
    with allure.step("Проверить, что поле зелёного цвета"):
        assert clr10 == green

    with allure.step("Закрыть окно браузера"):
        browser.quit()