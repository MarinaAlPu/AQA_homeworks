from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.saucedemo.com/")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys('standard_user')
driver.find_element(By.CSS_SELECTOR, '#password').send_keys('secret_sauce')

driver.find_element(By.CSS_SELECTOR, '#login-button').click()

driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-backpack').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-bolt-t-shirt').click()
driver.find_element(By.CSS_SELECTOR, '#add-to-cart-sauce-labs-onesie').click()

driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

driver.find_element(By.CSS_SELECTOR, '#checkout').click()

driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys("Marina")
driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys("Pudovkina")
driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys("123456")

driver.find_element(By.CSS_SELECTOR, '#continue').click()

result = driver.find_element(By.CSS_SELECTOR, 'div.summary_total_label').text

driver.quit()

def test_result():
    assert result == "Total: $58.29"