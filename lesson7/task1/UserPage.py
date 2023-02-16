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
    
# green = "rgba(209, 231, 221, 1)"
# red = "rgba(248, 215, 218, 1)"

#         locators = ['#first-name', '#last-name', '#address', '#zip-code', '#city',
#                     '#country', '#e-mail', '#phone', '#job-position', "#company"]
#         counter = 0
#         for counter in range(0, 10):
#             clr = self.browser.find_element(By.CSS_SELECTOR, locators[counter])
#             txt = clr.value_of_css_property("background-color").text
            
#             counter = counter + 1
#             return counter
#         print(counter)

            
                

#     def check_color(self):
#         green = "rgba(209, 231, 221, 1)"
#         red = "rgba(248, 215, 218, 1)"
          
#         @pytest.mark.parametrize( 'locator, result',
#         [('#first-name', green), ('#last-name', green), ('#address', green), ('#zip-code', red), ('#city', green),
#         ('#country', green), ('#e-mail', green), ('#phone', green), ('#job-position', green), ("#company", green)])
#         def check_the_color(locator, result):
#             color = self.browser.find_element(By.CSS_SELECTOR, locator).value_of_css_property("background-color")
#             assert color == result             


        # a = self._driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]') # взять браузер, найти элемент по локатору
        # txt = a.find_element(By.CSS_SELECTOR, 'b').text # у найденного элемента найти элемент по локатору
        # return int(txt) # у найденного элемента взять текст (количество книг) и преобразовать в число

 
        # locators = ['#first-name', '#last-name"', '#address',
        #         '#zip-code"]', '#city"]', '#"country"]',
        #         '#e-mail"]', '#phone"]', '#job-position"]', '#company"]']
        # colors = ['#first-name', '#last-name', '#address', '#zip-code', '#city',
        #           '#country', '#e-mail', '#phone', '#job-position', "#company"]
        # counter = 0
        # for counter in range(0, 10):
        #     self.browser.find_element(By.CSS_SELECTOR, locators[counter]).value_of_css_property("background-color")
        #     counter = counter + 1