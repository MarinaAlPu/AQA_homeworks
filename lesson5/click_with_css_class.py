from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

### CHROME ######################################################################################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# открыть страницу
driver.get("http://uitestingplayground.com/classattr")

driver.maximize_window()
sleep(1)
driver.execute_script("document.body.style.zoom = '80%'")
sleep(1)

# найти синюю кнопку 
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

# кликнуть на синюю(!) кнопку 3 раза
counter = 0
while counter < 3:
    blue_button.send_keys(Keys.ENTER) # или blue_button.click()?
    counter = counter + 1
    print("мы кликнули", int(counter), "раз")
    sleep(2)

    # избавиться от выпавшего окна
    Alert(driver).accept()
    sleep(1)

sleep(1)
driver.close()


### FIREFOX ######################################################################################
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

# открыть страницу
driver.get("http://uitestingplayground.com/classattr")

driver.maximize_window()
sleep(1)
driver.execute_script("document.body.style.zoom = '80%'")
sleep(1)

# найти синюю кнопку 
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

# кликнуть на синюю(!) кнопку 3 раза
counter = 0
while counter < 3:
    blue_button.send_keys(Keys.ENTER) # или blue_button.click()?
    counter = counter + 1
    print("мы кликнули", int(counter), "раз")
    sleep(2)

    # избавиться от выпавшего окна
    Alert(driver).accept()
    sleep(1)

sleep(1)
driver.close()