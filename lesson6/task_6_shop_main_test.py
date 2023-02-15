# Напишите автотест(!) на интернет-магазин
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть сайт
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
sleep(3)

# Авторизоваться под пользователем 'standard_user'
driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')
sleep(3)
driver.find_element(By.CSS_SELECTOR, '#login-button').click()
sleep(3)

# Добавить в корзину товары: 
# 1. Sauce Labs Backpack 
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
# 2. Sauce Labs Bolt T-Shirt 
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
# 3. Sauce Labs Onesie 
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()
sleep(3)

# Перейти в корзину
driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()
sleep(3)

# Нажать Checkout
driver.find_element(By.CSS_SELECTOR, '#checkout').click()
sleep(3)

# Заполнить форму своими данными:
# 1. Имя
# 2. Фамилия
# 3. Почтовый индекс
driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Marina")
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Pudovkina")
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")
sleep(3)

# Нажать Continue
driver.find_element(By.CSS_SELECTOR, '#continue').click()
sleep(3)

# Прочитать со страницы итоговую стоимость ( 'Total' )
txt = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text
print(txt)

# Проверить, что итоговая сумма равна 58.29 Total: $58.29
@pytest.mark.parametrize( 'locator, result',
    [('div.summary_total_label', "Total: $58.29")])
def test_background_color_green(locator, result):
    assert driver.find_element(By.CSS_SELECTOR, locator).text == result

# Закрыть браузер
#driver.quit()