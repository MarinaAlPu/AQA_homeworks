# Дождаться картинки
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# явное ожидание - ждём, когда появится картинка
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Перейти на сайт
driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

# Дождаться загрузки всех картинок
WebDriverWait(driver, 10, 0.1).until(
    EC.text_to_be_present_in_element( (By.CSS_SELECTOR, "#text"), "Done!") 
)

# Получить значение атрибута 'src' у 3й картинки. Вывести значение в консоль
print(driver.find_element(By.CSS_SELECTOR, "img:nth-of-type(3)").get_attribute("src"))

driver.quit()