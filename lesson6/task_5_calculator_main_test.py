# Автотест на калькулятор (запускается через 'pytest')
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()

# В поле ввода по локатору '#delay' ввести значение 45
driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

driver.find_element(By.XPATH, '//*[text()="C"]').click()

# Нажать на кнопки 7, +, 8, =
driver.find_element(By.XPATH, '//*[text()="7"]').click()
driver.find_element(By.XPATH, '//*[text()="+"]').click()
driver.find_element(By.XPATH, '//*[text()="8"]').click()
driver.find_element(By.XPATH, '//*[text()="="]').click()

waiter = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), "15") )

# Проверить (assert), что в окне отобразится результат '15' через 45 секунд.
@pytest.mark.parametrize( 'locator',
    [('.screen')
])
def test_result(locator):
    assert driver.find_element(By.CSS_SELECTOR, locator).text == "15"

#driver.quit()