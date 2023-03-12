import allure
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from task3.MainPage import MainPage
from task3.ShopPage import ShopPage
from task3.CartPage import CartPage
from task3.NamePage import NamePage
from task3.TotalPage import TotalPage

@allure.epic("Магазин")
@allure.suite("Оформление заказа")
@allure.title("Проверка процесса оформления заказа")
@allure.description("Проверка процесса оформления заказа и формирования общей суммы заказа")
@allure.feature("Получение общей сумма заказа")
@allure.severity("Blocker")
@allure.id("Shop-1") 
def test_cart_counter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)

    with allure.step("Авторизоваться"): 
        main_page.auth('standard_user', 'secret_sauce')
        main_page.login()

    with allure.step("Открылась страница магазина"):  
        shop_page = ShopPage(browser)

    shop_page.add_product()

    cart_page = CartPage(browser)
    cart_page.checkout()

    name_page = NamePage(browser)
    name_page.personal_data("Marina", "Pudovkina", "123456")
   

    total_page = TotalPage(browser)
    as_is = total_page.get_total()
    sleep(10)
    with allure.step("Проверить, что общая сумма заказа составляет $58.29"):  
        assert as_is == "Total: $58.29"

    with allure.step("Закрыть окно браузера"):  
        browser.quit()

