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

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
driver.maximize_window()

driver.find_element(By.CSS_SELECTOR, 'input[name="first-name"]').send_keys(str(user.my_first_name()))
driver.find_element(By.CSS_SELECTOR, 'input[name="last-name"]').send_keys(str(user.my_last_name()))
driver.find_element(By.CSS_SELECTOR, 'input[name="address"]').send_keys(str(user.my_address()))
driver.find_element(By.CSS_SELECTOR, 'input[name="zip-code"]').send_keys(str(user.my_zip_code()))
driver.find_element(By.CSS_SELECTOR, 'input[name="city"]').send_keys(str(user.my_city()))
driver.find_element(By.CSS_SELECTOR, 'input[name="country"]').send_keys(str(user.my_country()))
driver.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]').send_keys(str(user.my_email()))
driver.find_element(By.CSS_SELECTOR, 'input[name="phone"]').send_keys(str(user.my_phone_number()))
driver.find_element(By.CSS_SELECTOR, 'input[name="job-position"]').send_keys(str(user.my_job_position()))
driver.find_element(By.CSS_SELECTOR, 'input[name="company"]').send_keys(str(user.my_company()))

driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').send_keys(Keys.ENTER)

green = "rgba(209, 231, 221, 1)"
red = "rgba(248, 215, 218, 1)"

first_name_color = driver.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("background-color")
last_name_color = driver.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property("background-color")
address_color = driver.find_element(By.CSS_SELECTOR, '#address').value_of_css_property("background-color")
zip_code_color = driver.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
city_color = driver.find_element(By.CSS_SELECTOR, '#city').value_of_css_property("background-color")
country_color = driver.find_element(By.CSS_SELECTOR, '#country').value_of_css_property("background-color")
e_mail_color = driver.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color")
phone_color = driver.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("background-color")
job_position_color = driver.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property("background-color")
company_color = driver.find_element(By.CSS_SELECTOR, '#company').value_of_css_property("background-color")

# def test_background_color_green():
#     assert first_name_color == green
#     assert last_name_color == green
#     assert address_color == green
#     assert city_color == green
#     assert country_color == green
#     assert e_mail_color == green
#     assert phone_color == green
#     assert job_position_color == green
#     assert company_color == green

xxx = [first_name_color, last_name_color, address_color, city_color,
 country_color, e_mail_color, phone_color, job_position_color, company_color]

for x in xxx:
    assert x == green

def test_background_color_red():
    assert zip_code_color == red

driver.quit()