from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self.browser.implicitly_wait(4)
        self.browser.maximize_window() 

    def delay(self, time_for_delay):
        self.browser.find_element(By.CSS_SELECTOR, "#delay").clear()
        self.browser.find_element(By.CSS_SELECTOR, "#delay").send_keys(time_for_delay)

    def clear_entry_field(self):
        self.browser.find_element(By.XPATH, '//*[text()="C"]').click()    

    def input_data(self):
        locators = ['//*[text()="7"]', '//*[text()="+"]', '//*[text()="8"]', '//*[text()="="]']
        counter = 0
        for counter in range(0, 4):
            self.browser.find_element(By.XPATH, locators[counter]).click()
            counter = counter + 1

        waiter = WebDriverWait(self.browser, 46).until(EC.text_to_be_present_in_element( (By.CSS_SELECTOR, ".screen"), "15") )

    def check_result(self):
        result = self.browser.find_element(By.CSS_SELECTOR, ('.screen')).text
        return result