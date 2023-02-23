import requests
import random
from EmployeeApi import Employee

# base_url = "https://x-clients-be.onrender.com"

employee_api = Employee("https://x-clients-be.onrender.com")

def test_get_random_employee_list():
    employee_list = employee_api.get_random_employee_list()
    print(employee_list)
#    assert len(employee_list) > 0 

# 2. ДОБАВИТЬ НОВОГО СОТРУДНИКА
def test_add_new_employee():
# - получить список компаний
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

# - добить компанию
    name = 'Компания, давай уже удаляйся'
    description = '!!!!!!!'
    new_body = employee_api.add_new_company(name, description)
    new_company_id = new_body['id']

# - получить новый список компаний
    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)

# проверить, что стало компаний +1
    assert len_after - len_before == 1

# проверить название и описание последней компании (мы их передаём при создании)
# проверить, что id последней компании в списке равен ответу из шага 2
    assert company_list_after[-1]["name"] == name
    assert company_list_after[-1]["description"] == description
    assert company_list_after[-1]["id"] == new_company_id


# - Получить список сотрудников 
    employee_body_before = employee_api.get_employee_list(new_company_id)

# - Получить количество сотрудников
    staff_before = len(employee_body_before)

# добавить сотрудника
    company_id = new_company_id # убрать???
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanych"
    phone = "79123456789"
    url = "Какой-то url"

# - Добавить нового сотрудника
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

# - Получить новое количество сотрудников
    employee_body_after = employee_api.get_employee_list(new_company_id)
    staff_after = len(employee_body_after)

    assert staff_after - staff_before == 1

# - найти нового сотрудника по id
    id = new_employee_id
    info_employee = employee_api.get_employee_info(id)

    assert info_employee["companyId"] == company_id
    assert info_employee["firstName"] == first_name
    assert info_employee["lastName"] == last_name
    assert info_employee["middleName"] == middle_name
    assert info_employee["phone"] == phone
    assert info_employee["avatar_url"] == url

# - Удалить компанию
    resp = employee_api.delete_company(new_company_id)
#    print(resp)

# - Получить список компаний
    company_list_end = employee_api.get_company_list()
    len_end = len(company_list_end)
    assert len_before == len_end
#    assert len_end - len_before == 1

    # body = employee_api.get_company_list()
    # assert body[-1]["id"] != new_company_id # проверка, что последняя организация - не та, которую мы добавили.

# 3. ПОЛУЧИТЬ СОТРУДНИКА ПО ID
def test_get_employee_by_id():
    employee_list = employee_api.get_employee_list()
    assert len(employee_list) > 0 

# - Добавить нового сотрудника
    creds = { 
        'username':'roxy',
        'password': 'animal-fairy'
    }

    new_employee = {
        'companyId': random_id,
        'firstName': 'Ivan',
        'lastName': 'Ivanov',
        'middleName': 'Ivanych',
        'phone': '+79123456789',
        'url': 'some url'
    }

# - авторизация
    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]   
    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.post(base_url + '/employee', json=new_employee, headers = my_headers)
    assert resp.status_code == 201
    new_employee_id = resp.json()['id']
    print("нового сотрудника id: " + str(new_employee_id))

# - Получить список id сотрудников
    id = new_employee_id


# - Получить информацию по любому id сотрудника (получаю по id добавленного сотрудника)
    resp = requests.get(base_url + '/employee/' + str(new_employee_id))
    info_employee = resp.json()
    print("информация о сотруднике: " + str(info_employee))

# - Проверить код  ответа
    assert resp.status_code == 200

# - Проверить, что ???



# 4. ИЗМЕНИТЬ ИНФОРМАЦИЮ О СТОРУДНИКЕ
def test_change_info_employee():
# - получить список компаний
    employee_list_before = employee_api.get_employee_list()
    len_before = len(employee_list_before)

# - добить компанию
    name = 'Проверяю, что компания удаляется'
    description = 'А она не удаляется'
    new_body = employee_api.add_new_company(name, description)
    new_company_id = new_body['id']

# - получить новый список компаний
    employee_list_after = employee_api.get_employee_list()
    len_after = len(employee_list_after)

# проверить, что стало компаний +1
    assert len_after - len_before == 1

# - Получить список сотрудников 
    employee_body_before = employee_api.get_employee_list(new_company_id)

# - Получить количество сотрудников
    staff_before = len(employee_body_before)

# добавить сотрудника
    company_id = new_company_id # убрать???
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanych"
    phone = "79123456789"
    url = "Какой-то url"

# - Добавить нового сотрудника
    new_employee_body = employee_api.add_new_employye(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

# - Получить новое количество сотрудников
    employee_body_after = employee_api.get_employee_list(new_company_id)
    staff_after = len(employee_body_after)

    assert staff_after - staff_before == 1

# - найти нового сотрудника по id
    id = new_employee_id
    info_employee = employee_api.get_employee_info(id)

    assert info_employee["companyId"] == company_id
    assert info_employee["firstName"] == first_name
    assert info_employee["lastName"] == last_name
    assert info_employee["middleName"] == middle_name
    assert info_employee["phone"] == phone
    assert info_employee["url"] == url



# - Изменить информацию о сотруднике
    change_employee = {
        'lastName': 'спать уже пора давно',
        'email': 'new@test.ru',
        'url': 'не будет url',
        'isActive': True
    }

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json=change_employee, headers = my_headers)
    assert resp.status_code == 200

# - Получить изменённую информацию о сотруднике
    resp = requests.get(base_url + '/employee/' + str(new_employee_id))
    info_employee = resp.json()
    print("информация по изменённому сотруднику, полученная по id:")
    print(info_employee)

# - Проверить код ответа
    assert resp.status_code == 200

# - Проверить, что новые данные сотрудника равны данным, внесённым при изменении.
    response_body = resp.json()
    my_employee_last_name = response_body["last_name"]
    my_employee_email = response_body["email"]
    my_employee_url = response_body["avatar_url"]
    my_employee_is_active = response_body["isActive"]

    print(my_employee_last_name)
    print(my_employee_email)
    print(my_employee_url)
    print(my_employee_is_active)

    assert my_employee_last_name == 'спать уже пора давно'
    assert my_employee_email == 'new@test.ru'
    assert my_employee_url == 'не будет url'
    assert my_employee_is_active == True

# - Удалить компанию
    employee_api.delete_company(new_company_id)

# - Получить список компаний
    # employee_list_end = employee_api.get_employee_list()
    # len_end = len(employee_list_end)
    
    # assert len_before == len_end

