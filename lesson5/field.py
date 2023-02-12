from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#from selenium.common.exceptions import NoSuchElementException

### CHROME ######################################################################################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# открыть окно
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()

# найти поле ввода
field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

# ввести в поле текст `1000`
field.send_keys("1000", Keys.RETURN)
sleep(2)

# очистить поле ввода
field.clear()
sleep(2)
field.send_keys("SkyPro", Keys.ENTER)

print("В Chrome поле ввода не принимает текст")

sleep(2)
driver.close()


### FIREFOX ######################################################################################
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

# открыть окно
driver.get("http://the-internet.herokuapp.com/inputs")
driver.maximize_window()

# найти поле ввода
field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')

# ввести в поле текст `1000`
field.send_keys("1000", Keys.RETURN)
sleep(2)

# очистить поле ввода
field.clear()
sleep(2)

# ввести в поле ввода текст `SkyPro`
field.send_keys("SkyPro", Keys.RETURN)
sleep(2)

print("It's alive!!!")

sleep(2)
driver.close()





# print(field.get_attribute("type"))