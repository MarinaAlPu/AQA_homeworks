from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# создаём класс методов на странице с результатом поиска книг 
# класс ResultPage умеет переключаться на таблицу и добавлять книги в корзину

class ResultPage:

    def __init__(self, browser):
        self._driver = browser # внутренняя переменная

    def switch_to_table(self):
    # переключиться на режим "таблица"
        self._driver.find_element(By.CSS_SELECTOR, 'a[title="таблицей"]').click()    
    # ждём, когда на странице появится таблица
        WebDriverWait(self._driver, 10).until(
            EC.presence_of_element_located( (By.CSS_SELECTOR, 'table') )
        )

    def add_books(self):
    # добавить все книги и посчитать сколько их 
        buy_buttons = self._driver.find_elements(By.CSS_SELECTOR, '.btn.buy-link.btn-primary') # хотим собрать все - find_elementS !!!
        print(len(buy_buttons))
        counter = 0
        for btn in buy_buttons: # взять список кнопок и по каждой кликнуть
            btn.click()
            counter = counter +1
            return counter # чтобы вынести counter из медота в глобальную область
        print(counter)


    def get_empty_result_message(self):
        div = self._driver.find_element(By.CSS_SELECTOR, 'div.search-error')
        h1 = div.find_element(By.CSS_SELECTOR, 'h1')
        return h1.text
    
    
