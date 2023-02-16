from selenium.webdriver.common.by import By

# создаём класс методов, которые используются на главной странице

class MainPage:
    # конструктор - это метод, который вызывается один раз при создании нового экземпляра класса 
    # он срабатывает на этой строке main_page = MainPage(); в labirint_page_object_test.py
    def __init__(self, driver):
        self._driver = driver
        self._driver.get("https://www.labirint.ru/") # браузер создаётся и сразу идёт на сайт
        self._driver.implicitly_wait(4) # неявное ожидание, на всякий случай, когда что-то не доехало
        self._driver.maximize_window() # окно разворачивается
        
    def set_cookie_policy(self): # метод, который вызываем, а драйвер понимает, что надо проставить cookie_policy = 1
        # нам надо, чтобы внутри этого метода было обращение к браузеру add cookie 
        # но класс MainPage ничего не знает о браузере, значит надо ему это передать в конструктор 
        # пишем конструктор __init__        
        # после добавления driver в конструтор мы можем обращаться к драйверу
        
        cookie = {                         # чтобы не всплывала плашка про куки
            'name' : 'cookie_policy',
            'value' : '1'
        }
        self._driver.add_cookie(cookie) # этот метод есть у драйвера 
                                        # в файле labirint_methods_test.py метод open_labirint (browser.add_cookie(my_cookie) ) 
                                        # где взять cookie? - в labirint_methods_test.py есть объект cookie 
                                        # несём его сюда перед этой строчкой
        
# получилось: когда вызываем метод set_cookie_policy вызывается драйвер,
# а у драйвера вызывается метод add_cookie с переменной cookie

# как драйвер попадает в класс MainPage?
# мы должны передать этот параметр в конструктор в этой строке main_page = MainPage(browser) в файле labirint_page_object_test.py

#        print("меня вызвали") # проверяем, что всё работает

    def search(self, term):
# говорим внутреннему драйверу найти элемент 
# драйвер нам доступен по self._driver
        # найти все книги по слову Python - меняем на term, т.к. поиск каждый раз разный
        self._driver.find_element(By.CSS_SELECTOR, "#search-field").send_keys(term)
        self._driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
        