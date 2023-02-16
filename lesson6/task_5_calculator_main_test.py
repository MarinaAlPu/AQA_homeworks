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

driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, "#delay").clear()
driver.find_element(By.CSS_SELECTOR, "#delay").send_keys("45")

driver.find_element(By.XPATH, '//*[text()="C"]').click()

driver.find_element(By.XPATH, '//*[text()="7"]').click()
driver.find_element(By.XPATH, '//*[text()="+"]').click()
driver.find_element(By.XPATH, '//*[text()="8"]').click()
driver.find_element(By.XPATH, '//*[text()="="]').click()

waiter = WebDriverWait(driver, 46).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), "15") )

sum = driver.find_element(By.CSS_SELECTOR, '.screen').text

def test_result():
    assert str(sum) == "15"

driver.quit()