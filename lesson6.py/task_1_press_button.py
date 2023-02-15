# Нажатие на кнопку
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.implicitly_wait(16) # неявное ожидание - в браузере, ждём и ищем объект, нет условий

# Перейти на страницу
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
driver.find_element(By.CSS_SELECTOR, "#ajaxButton").click()

# Получить текст из зеленой плашки. Вывести текст в консоль (”Data loaded with AJAX get request.”)
print(driver.find_element(By.CSS_SELECTOR, 'p.bg-success').text) # находим зелёную плашку и получаем из неё текст

driver.quit()