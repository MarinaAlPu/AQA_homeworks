from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from task1.MainPage import MainPage
from task1.UserPage import UserPage

def test_user_form():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    main_page = MainPage(browser)
    main_page.input_data()
    main_page.click_button()
    
    user_page = UserPage(browser)

    green = "rgba(209, 231, 221, 1)"
    red = "rgba(248, 215, 218, 1)"

    clr1 = user_page.get_color1()
    assert clr1 == green

    clr2 = user_page.get_color2()
    assert clr2 == green

    clr3 = user_page.get_color3()
    assert clr3 == green

    clr4 = user_page.get_color4()
    assert clr4 == red

    clr5 = user_page.get_color5()
    assert clr5 == green

    clr6 = user_page.get_color6()
    assert clr6 == green

    clr7 = user_page.get_color7()
    assert clr7 == green

    clr8 = user_page.get_color8()
    assert clr8 == green

    clr9 = user_page.get_color9()
    assert clr9 == green

    clr10 = user_page.get_color10()
    assert clr10 == green

    #browser.quit()