from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.common.exceptions import NoSuchElementException

### CHROME ######################################################################################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# открыть страницу
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()

# найти поле usrname
username_field = driver.find_element(By.CSS_SELECTOR, "#username")

# в поле usrname ввести значение tomsmith
username_field.send_keys("tomsmith")
sleep(1)

# найти поле password 
password_field = driver.find_element(By.CSS_SELECTOR, "#password")

# в поле password ввести значение SuperSecretPassword!
password_field.send_keys("SuperSecretPassword!")
sleep(1)

# наqnb кнопку `Login`
login_button = driver.find_element(By.CSS_SELECTOR, "i.fa-sign-in")

# нажать кнопку `Login`
login_button.click()
sleep(1)

print("Мы авторизировались")

sleep(1)
driver.close()

### FIREFOX ######################################################################################
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()

# найти поле usrname
username_field = driver.find_element(By.CSS_SELECTOR, "#username")

# в поле usrname ввести значение tomsmith
username_field.send_keys("tomsmith")
sleep(1)

# найти поле password 
password_field = driver.find_element(By.CSS_SELECTOR, "#password")

# в поле password ввести значение SuperSecretPassword!
password_field.send_keys("SuperSecretPassword!")
sleep(1)

# наqnb кнопку `Login`
login_button = driver.find_element(By.CSS_SELECTOR, "i.fa-sign-in")

# нажать кнопку `Login`
login_button.click()
sleep(1)

print("Мы авторизировались")

sleep(1)
driver.close()

#######################################################################################
# проверить наличие элемента на странице
# def find_button_logout():
#     try:
#         driver.find_element(By.CSS_SELECTOR, "i.icon-signout")
#     except NoSuchElementException:
#         return False
#     return True

# if (find_button_logout() == True):
#     print("Мы авторизировались")
# else:
#     print("Мы не авторизировались")