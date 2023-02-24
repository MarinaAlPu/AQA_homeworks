import pytest
from string_utils import StringUtils

#capitilize() - принимает на вход текст, делает первую букву заглавной и возвращает этот же текст
@pytest.mark.capitilize_test
@pytest.mark.positive_test
@pytest.mark.parametrize("text_in, text_out", 
    [("домашняя работа", "Домашняя работа"),
    ("knowledge", "Knowledge"),
    ("dомашняя работа", "Dомашняя работа"),
    ("жnowledge", "Жnowledge"),
    ("ёжик", "Ёжик"),
    ("йожик", "Йожик")
    ])
def test_capitilize_positive(text_in, text_out):
    stringUtils = StringUtils()
    res = stringUtils.capitilize(text_in)
    assert res == text_out


# moveprefix() - принимает на вход текст и удаляет префикс (тут - пробелы в начале, если они есть)
@pytest.mark.positive_test
@pytest.mark.parametrize("text_in, text_out", 
    [(" knowledge", "knowledge"),
     ("  knowledge", "knowledge"),
     ("knowledge", "knowledge"),
     ("                                                                    knowledge", "knowledge")])
def test_trim_positive(text_in, text_out):
    stringUtils = StringUtils()
    res = stringUtils.trim(text_in)
    assert res == text_out


# Принимает на вход текст с разделителем и возвращает список строк.
@pytest.mark.to_list_test
@pytest.mark.positive_test
@pytest.mark.parametrize("string, text_out",
    [
    ("a,b,c,d", ["a", "b", "c", "d"])
     ])
def test_to_list_positive(string, text_out):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string)
    assert res == text_out

@pytest.mark.to_list_test
@pytest.mark.positive_test
@pytest.mark.parametrize("string, delimeter, text_out",
    [
    ("1:2:3:4", "2", ["1:", ":3:4"]),
    ("1:2 3:4:5:6,7", ":", ["1", "2 3", "4", "5", "6,7"]),
    ("1:2:3:4⛄5:6:7", "⛄", ["1:2:3:4", "5:6:7"]),
    ("разделитель пробел", " ", ["разделитель", "пробел"]),
    ("буква цифра спецсимвол знак препинания смайлик", "а", ["букв", " цифр", " спецсимвол зн", "к препин", "ния см", "йлик"]),
    ("разделитель, по умолчанию - запятая", "умолчанию", ["разделитель, по ", " - запятая"]),
    ("Windows Android какая-то ОС Safari", "какая-то ОС", ["Windows Android ", " Safari"]),
    ("Windows Android Safari!", "!", ["Windows Android Safari", ""]),
    ("?Windows Android Safari", "?", ["", "Windows Android Safari"]),
    ("м", "м", ["", ""]),
    ("", "", [])
     ])
def test_to_list_positive(string, delimeter, text_out):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimeter)
    assert res == text_out   

@pytest.mark.to_list_test
@pytest.mark.xfail#(strict=True)
@pytest.mark.negative_test
@pytest.mark.parametrize("string, delimeter, text_out",
    [
    ("a,b,c,d", "", ["a", "b", "c", "d"]),
    ("", "", ["", ""])
     ])
def test_to_list_negative(string, delimeter, text_out):
    stringUtils = StringUtils()
    res = stringUtils.to_list(string, delimeter)
    assert res == text_out    


# Возвращает `True`, если строка содержит искомый символ и `False` - если нет 
@pytest.mark.contains_test
@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result",
    [("string", "r", True),
    ("string", "q", False),
    ("строка", "а", True),
    ("строка", "ю", False),
    ("12345", "3", True),
    ("123", "7", False),
    ("молоко", "о", True),
    ("таёжный", "ё", True),
    ("таёжный", "й", True),    
    ("фраза из нескольких languages", "а", True), # русская а
    ("фраза из нескольких languages", "a", True), # английская a  
    ("строка с несколькими словами", "а", True),
    ("aнглийскaя a в русском тексте, a ищем русскую",  "a", True), # английская a 
    ("fgsоfbоо dfbо", "о", True), # русская о 
    ("1, 2, 3", "", True), # ищем пустую строку
    ("ищем пробел", " ", True),
    ("", "", True), # ищем пустую строку
    ("⛄", "⛄", True)
    ])
def test_contains_positive(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)    
    assert res == result

@pytest.mark.contains_test
@pytest.mark.negative_test
@pytest.mark.xfail(strict=True)
@pytest.mark.parametrize("string, symbol, result",
    [("string", "r", False),
    ("123456", "3", False),
    ("000000", "1", True),
    ("строка", "ю", True),
    ("стрОка", "0", True), # ищем 0
    ])
def test_contains_negative(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.contains(string, symbol)    
    assert res == result


# даляет все подстроки из переданной строки  
@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, text_out",
    [
    ("SkyPro", "k", "SyPro"),
    ("помидор", "о", "пмидр"),
    ("Sky Pro", " ", "SkyPro"),
    ("125266721", "2", "156671"),
    ("Sky, Pro", ",", "Sky Pro"),
    ("помидор⛄", "⛄", "помидор"),
    ("помидор", "помидор", ""),
    ("", "", "")
    ])    
def test_delete_symbol_positive(string, symbol, text_out):
    stringUtils = StringUtils()
    res = stringUtils.delete_symbol(string, symbol)
    assert res == text_out


# Возвращает `True`, если строка начинается с заданного символа и `False` - если нет 
@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result",
    [
    ("холодильник", "х", True),
    ("холодильник", "ь", False),
    ("milk", "m", True),
    ("ёж", "ё", True),
    ("йогурт", "й", True),  
    ("холодильник", "x", False), # английская x
    ("127milk", "1", True),
    ("", "", True)
    ])
def test_starts_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.starts_with(string, symbol)
    assert res == result


# Возвращает `True`, если строка заканчивается заданным символом и `False` - если нет 
@pytest.mark.positive_test
@pytest.mark.parametrize("string, symbol, result",
    [
    ("string", "g", True),
    ("string", "s", False),
    ("стол", "л", True),
    ("мумиё", "ё", True),
    ("таёжный", "й", True),  
    ("стол", "с", False),
    ("string", "", True),
    ("", "", True)
    ])
def test_end_with(string, symbol, result):
    stringUtils = StringUtils()
    res = stringUtils.end_with(string, symbol)
    assert res == result
  

# Возвращает `True`, если строка пустая и `False` - если нет 
@pytest.mark.positive_test
@pytest.mark.parametrize("text_in, result",
    [
    ("", True),
    (" ", True),
    ("непустая строка", False),
    ("string isn't empty", False),
    ("☮", False),
    (" string isn't empty ", False),
    ("      string isn't empty      ", False)
    ])    
def test_is_empty(text_in, result):
    stringUtils = StringUtils()
    res = stringUtils.is_empty(text_in)
    assert res == result


# Преобразует список элементов в строку с указанным разделителем 
@pytest.mark.positive_test
@pytest.mark.parametrize("lst, string_out",
    [
    (["Sky", "Pro"], "Sky, Pro"),
    ])
def test_list_to_string_positive_default(lst, string_out):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst)
    assert res ==  string_out

@pytest.mark.positive_test
@pytest.mark.parametrize("lst, joiner, string_out",
    [
    (["Sky", "Pro"], ", ", "Sky, Pro"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    (["строка", "с", "разделителем", "пробел"], " ", "строка с разделителем пробел"),
    ([], "", ""),
    ([""], "", "")    
    ])
def test_list_to_string_positive(lst, joiner, string_out):
    stringUtils = StringUtils()
    res = stringUtils.list_to_string(lst, joiner)
    assert res ==  string_out
