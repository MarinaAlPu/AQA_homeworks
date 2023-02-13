from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу 
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()

# Кликнуть на синюю кнопку
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn")

# кликнуть кнопку 3 раза
counter = 0
while counter < 3:
    blue_button.send_keys(Keys.ENTER)
    counter = counter + 1
    print("мы кликнули", int(counter), "-й раз")
    sleep(2)
    driver.find_element(By.CSS_SELECTOR, "body") # снимаем выделение с синей кнопки
    sleep(2)

sleep(2)
driver.close()