import allure
import pytest
from selenium.webdriver.common.by import By

class UserPage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.implicitly_wait(4)
    
    @allure.step("Получить цвет поля 'First name'")
    def get_color1(self) -> str:
        clr1 = self.browser.find_element(By.CSS_SELECTOR, '#first-name').value_of_css_property("background-color")
        return clr1
    
    @allure.step("Получить цвет поля 'Last name'")
    def get_color2(self) -> str:    
        clr2 = self.browser.find_element(By.CSS_SELECTOR, '#last-name').value_of_css_property("background-color")
        return clr2
    
    @allure.step("Получить цвет поля 'Address'")
    def get_color3(self) -> str:    
        clr3 = self.browser.find_element(By.CSS_SELECTOR, '#address').value_of_css_property("background-color")
        return clr3
    
    @allure.step("Получить цвет поля 'Zip code'")
    def get_color4(self) -> str:    
        clr4 = self.browser.find_element(By.CSS_SELECTOR, '#zip-code').value_of_css_property("background-color")
        return clr4

    @allure.step("Получить цвет поля 'City'")
    def get_color5(self) -> str:    
        clr5 = self.browser.find_element(By.CSS_SELECTOR, '#city').value_of_css_property("background-color")
        return clr5

    @allure.step("Получить цвет поля 'Country'")
    def get_color6(self) -> str:    
        clr6 = self.browser.find_element(By.CSS_SELECTOR, '#country').value_of_css_property("background-color")
        return clr6

    @allure.step("Получить цвет поля 'E-mail'")
    def get_color7(self) -> str:    
        clr7 = self.browser.find_element(By.CSS_SELECTOR, '#e-mail').value_of_css_property("background-color")
        return clr7

    @allure.step("Получить цвет поля 'Phone number'")
    def get_color8(self) -> str:    
        clr8 = self.browser.find_element(By.CSS_SELECTOR, '#phone').value_of_css_property("background-color")
        return clr8
    
    @allure.step("Получить цвет поля 'Job position'")
    def get_color9(self) -> str:    
        clr9 = self.browser.find_element(By.CSS_SELECTOR, '#job-position').value_of_css_property("background-color")
        return clr9

    @allure.step("Получить цвет поля 'Company'")
    def get_color10(self) -> str:    
        clr10 = self.browser.find_element(By.CSS_SELECTOR, "#company").value_of_css_property("background-color")
        return clr10