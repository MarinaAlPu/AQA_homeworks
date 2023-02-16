import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

class UserPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(4)
    
    def get_color1(self):
        clr1 = self.browser.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("background-color")
        return clr1
    
    def get_color2(self):    
        clr2 = self.browser.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property("background-color")
        return clr2
    
    def get_color3(self):    
        clr3 = self.browser.find_element(By.CSS_SELECTOR, '#address').value_of_css_property("background-color")
        return clr3
    
    def get_color4(self):    
        clr4 = self.browser.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
        return clr4

    def get_color5(self):    
        clr5 = self.browser.find_element(By.CSS_SELECTOR, '#city').value_of_css_property("background-color")
        return clr5

    def get_color6(self):    
        clr6 = self.browser.find_element(By.CSS_SELECTOR, '#country').value_of_css_property("background-color")
        return clr6

    def get_color7(self):    
        clr7 = self.browser.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color")
        return clr7

    def get_color8(self):    
        clr8 = self.browser.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("background-color")
        return clr8
    
    def get_color9(self):    
        clr9 = self.browser.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property("background-color")
        return clr9

    def get_color10(self):    
        clr10 = self.browser.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
        return clr10