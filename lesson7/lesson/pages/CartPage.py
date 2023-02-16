from selenium.webdriver.common.by import By

# создаём класс методов, которые работают в корзине

class CartPage:
    # 
    def __init__(self, browser):
        # говорим ему запомнить себе внутри , что есть драйвер
        self._driver = browser

    def get(self):
# перейти в корзину
    # вместо того, чтобы находить элемент по селектору и кликать, говорим перейти на страницу корзины
        # так можно делать если нет задачи проверить, что корзина кликается
        self._driver.get("https://www.labirint.ru/cart/")

    def get_counter(self):
# проверить, что счётчик товаров соответствует количеству добавленных
    # получить текущее значение счётчика в корзине
        a = self._driver.find_element(By.CSS_SELECTOR, 'a[data-event-label="myCart"]') # взять браузер, найти элемент по локатору
        txt = a.find_element(By.CSS_SELECTOR, 'b').text # у найденного элемента найти элемент по локатору
        return int(txt) # у найденного элемента взять текст (количество книг) и преобразовать в число
