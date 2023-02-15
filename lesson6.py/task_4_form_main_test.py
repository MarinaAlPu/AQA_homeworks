# Автотест на заполнение формы (запускается через 'pytest')
import pytest
from task_4_form_class import Users
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = Users("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "123@test.ru", "+79123456789", "QA", "SkyPro")

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Открыть страницу
driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window()

# Заполнить форму значениями

driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(str(user.myFirstName()))
driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(str(user.myLastName()))
driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(str(user.myAddress()))
driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(str(user.myZipCode()))
driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(str(user.myCity()))
driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(str(user.myCountry()))
driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(str(user.myEmail()))
driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(str(user.myPhoneNumber()))
driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(str(user.myJobPosition()))
driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(str(user.myCompany()))

# Нажать кнопку Submit
driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').send_keys(Keys.ENTER)
sleep(3)

# Проверить, что поле 'Zip code' подсвечено красным, остальные поля подсвечены зеленым
green = "rgba(209, 231, 221, 1)"
red = "rgba(248, 215, 218, 1)"
@pytest.mark.parametrize( 'locator, result',
    [('#first-name', green), ('#last-name', green), ('#address', green), ('#zip-code', red), ('#city', green),
     ('#country', green), ('#e-mail', green), ('#phone', green), ('#job-position', green), ("#company", green)])
def test_background_color_green(locator, result):
    assert driver.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color") == result

# driver.quit()