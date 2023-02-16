from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from task2.MainPage import MainPage

def test_calculator():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    main_page = MainPage(browser)
    main_page.delay("45")
    main_page.clear_entry_field()
    main_page.input_data()
    as_is = main_page.check_result()

    assert as_is == "15"

    #browser.quit()