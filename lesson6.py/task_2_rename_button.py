# Переименовать кнопку
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейти на сайт
driver.get("http://uitestingplayground.com/textinput")

# Указать в поле ввода текст "SkyPro"
driver.find_element(By.CSS_SELECTOR, "#newButtonName").send_keys("SkyPro")

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#updatingButton").click()

# Получить текст кнопки и вывести в консоль ("SkyPro")
print(driver.find_element(By.CSS_SELECTOR, "#updatingButton").text)

driver.quit()