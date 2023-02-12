from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

### CHROME ######################################################################################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# найти кнопку
search_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')

# кликнуть кнопку 5 раз
counter = 0
while counter < 5:
    search_button.send_keys(Keys.ENTER) # или search_button.click()?
    counter = counter + 1
    sleep(1)
print("мы кликнули", int(counter), "раз")

# Собрать со страницы список кнопок `Delete`
search_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")

# Вывести на экран размер списка
print(len(search_buttons))

sleep(1)
driver.close()


### FIREFOX ######################################################################################
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.maximize_window()

# Открыть страницу
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# найти кнопку
search_button = driver.find_element(By.CSS_SELECTOR, 'button[onclick="addElement()"]')

# кликнуть кнопку 5 раз
counter = 0
while counter < 5:
    search_button.send_keys(Keys.ENTER) # или search_button.click()?
    counter = counter + 1
    sleep(1)
print("мы кликнули", int(counter), "раз")

# Собрать со страницы список кнопок `Delete`
search_buttons = driver.find_elements(By.CSS_SELECTOR, ".added-manually")

# Вывести на экран размер списка
print(len(search_buttons))

sleep(1)

driver.close()
