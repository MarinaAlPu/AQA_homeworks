from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


from task3.MainPage import MainPage
from task3.ShopPage import ShopPage
from task3.CartPage import CartPage
from task3.NamePage import NamePage
from task3.TotalPage import TotalPage

def test_cart_caunter():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    main_page = MainPage(browser)
    main_page.auth()
    main_page.login()

    shop_page = ShopPage(browser)
    shop_page.add_product()

    cart_page = CartPage(browser)
    cart_page.checkout()

    name_page = NamePage(browser)
    name_page.personal_data()

    total_page = TotalPage(browser)
    as_is = total_page.get_total()

    assert as_is == "Total: $58.29"

    #browser.quit()