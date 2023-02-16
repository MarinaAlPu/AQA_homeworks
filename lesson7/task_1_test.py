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

    clr1 = user_page.get_color1()
    assert clr1 == "rgba(209, 231, 221, 1)"

    clr2 = user_page.get_color2()
    assert clr2 == "rgba(209, 231, 221, 1)"

    clr3 = user_page.get_color3()
    assert clr3 == "rgba(209, 231, 221, 1)"

    clr4 = user_page.get_color4()
    assert clr4 == "rgba(248, 215, 218, 1)"

    clr5 = user_page.get_color5()
    assert clr5 == "rgba(209, 231, 221, 1)"

    clr6 = user_page.get_color6()
    assert clr6 == "rgba(209, 231, 221, 1)"

    clr7 = user_page.get_color7()
    assert clr7 == "rgba(209, 231, 221, 1)"

    clr8 = user_page.get_color8()
    assert clr8 == "rgba(209, 231, 221, 1)"

    clr9 = user_page.get_color9()
    assert clr9 == "rgba(209, 231, 221, 1)"

    clr10 = user_page.get_color10()
    assert clr10 == "rgba(209, 231, 221, 1)"

    #browser.quit()