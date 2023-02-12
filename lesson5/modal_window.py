from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

### CHROME ######################################################################################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()

sleep(2)

# нажать кнопку 'Сlose' в модальном окне
button_close = driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

print("мы нажали кнопку 'Сlose'")

sleep(2)
driver.close()


### FIREFOX ######################################################################################
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

# открыть страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")
driver.maximize_window()

sleep(2)

# нажать кнопку 'Сlose' в модальном окне
button_close = driver.find_element(By.CSS_SELECTOR, "div.modal-footer").click()

print("мы нажали кнопку 'Сlose'")

sleep(2)
driver.close()