import pytest
import requests
from newEmployeeApi import Employee

base_url = "https://x-clients-be.onrender.com"

def test_get_random_employee_list():
    employee_api = Employee(base_url)
    employee_list = employee_api.get_random_employee_list()
    assert len(employee_list) >= 0    


def test_get_specific_employee_list():
    employee_api = Employee(base_url)
    id = 1290
    employee_list = employee_api.get_specific_employee_list(id)
    assert len(employee_list) > 0
    

def test_add_new_employee():
    employee_api = Employee(base_url)
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

    name = 'Компания для удаления'
    description = 'Хоть бы удалилась'
    new_body = employee_api.add_new_company(name, description)
    new_company_id = new_body['id']

    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)
    assert len_after - len_before == 1
    assert company_list_after[-1]["name"] == name
    assert company_list_after[-1]["description"] == description
    assert company_list_after[-1]["id"] == new_company_id

    employee_body_before = employee_api.get_specific_employee_list(new_company_id)
    staff_before = len(employee_body_before)

    company_id = new_company_id
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanych"
    phone = "79123456789"
    url = "his url"
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

    employee_body_after = employee_api.get_specific_employee_list(new_company_id)
    staff_after = len(employee_body_after)
    assert staff_after - staff_before == 1

    id = new_employee_id
    info_employee = employee_api.get_employee_info(id)
    assert info_employee["companyId"] == company_id
    assert info_employee["firstName"] == first_name
    assert info_employee["lastName"] == last_name
    assert info_employee["middleName"] == middle_name
    assert info_employee["phone"] == phone
    assert info_employee["avatar_url"] == url

    id = new_company_id
    deleted_company = employee_api.delete_company(id)
    assert deleted_company["id"] == new_company_id
    assert deleted_company["isActive"] == True
    assert deleted_company["name"] == name
    assert deleted_company["description"] == description

    company_list_end = employee_api.get_company_list()
    len_end = len(company_list_end)
    assert len_before == len_end
    assert company_list_end[-1]["id"] != new_company_id


def test_get_employee_by_id():
    employee_api = Employee(base_url)
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

    name = 'Компания для удаления'
    description = 'Хоть бы удалилась'
    new_body = employee_api.add_new_company(name, description)
    new_company_id = new_body['id']

    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)
    assert len_after - len_before == 1
    assert company_list_after[-1]["name"] == name
    assert company_list_after[-1]["description"] == description
    assert company_list_after[-1]["id"] == new_company_id

    employee_body_before = employee_api.get_specific_employee_list(new_company_id)
    staff_before = len(employee_body_before)

    company_id = new_company_id
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanych"
    phone = "79123456789"
    url = "Какой-то url"
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

    employee_body_after = employee_api.get_specific_employee_list(new_company_id)
    staff_after = len(employee_body_after)
    assert staff_after - staff_before == 1

    id = new_employee_id
    info_employee = employee_api.get_employee_info(id)
    assert info_employee["companyId"] == company_id
    assert info_employee["firstName"] == first_name
    assert info_employee["lastName"] == last_name
    assert info_employee["middleName"] == middle_name
    assert info_employee["phone"] == phone
    assert info_employee["avatar_url"] == url

    id = new_company_id
    deleted_company = employee_api.delete_company(id)
    assert deleted_company["id"] == new_company_id
    assert deleted_company["isActive"] == True
    assert deleted_company["name"] == name
    assert deleted_company["description"] == description

    company_list_end = employee_api.get_company_list()
    len_end = len(company_list_end)
    assert len_before == len_end
    assert company_list_end[-1]["id"] != id


def test_change_info_employee():
    employee_api = Employee(base_url)
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

    name = 'Компания для удаления'
    description = 'Хоть бы удалилась'
    new_body = employee_api.add_new_company(name, description)
    new_company_id = new_body['id']

    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)
    assert len_after - len_before == 1
    assert company_list_after[-1]["name"] == name
    assert company_list_after[-1]["description"] == description
    assert company_list_after[-1]["id"] == new_company_id

    employee_body_before = employee_api.get_specific_employee_list(new_company_id)
    staff_before = len(employee_body_before)

    company_id = new_company_id
    first_name = "Иван"
    last_name = "Иванов"
    middle_name = "Иваныч"
    phone = "79123456789"
    url = "Какой-то url"
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

    employee_body_after = employee_api.get_specific_employee_list(new_company_id)
    staff_after = len(employee_body_after)
    assert staff_after - staff_before == 1


    id = new_employee_id
    info_employee = employee_api.get_employee_info(id)
    assert info_employee["companyId"] == company_id
    assert info_employee["firstName"] == first_name
    assert info_employee["lastName"] == last_name
    assert info_employee["middleName"] == middle_name
    assert info_employee["phone"] == phone
    assert info_employee["avatar_url"] == url

    new_last_name = "Новая фамилия"
    new_email = "new@test.ru"
    new_url = "новый url"
    new_is_active = True
    changed_employee = employee_api.change_employee_info(new_employee_id, new_last_name, new_email, new_url, new_is_active)

    id = new_employee_id
    changed_employee = employee_api.get_employee_info(id)
    assert changed_employee["isActive"] == new_is_active
    assert changed_employee["id"] == new_employee_id
    assert changed_employee["email"] == new_email
    assert changed_employee["avatar_url"] == new_url

    id = new_company_id
    deleted_company = employee_api.delete_company(id)
    assert deleted_company["id"] == new_company_id
    assert deleted_company["isActive"] == True
    assert deleted_company["name"] == name
    assert deleted_company["description"] == description

    company_list_end = employee_api.get_company_list()
    len_end = len(company_list_end)
    assert len_before == len_end
    assert company_list_end[-1]["id"] != id


@pytest.mark.parametrize("new_employee, status_code",
    [
    ({'company_id': '', 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': None, 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),
    
    ({'company_id': 'company_id', 'first_name': None, 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': None, 
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': None, 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'phone': None, 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': None}, 400)
    ])
def test_add_employees(new_employee, status_code):
    employee_api = Employee(base_url)
    creds = { 
        'username' : 'roxy',
        'password' : 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.post(base_url + "/company", json={'name': 'Company For Employees', 'description': 'Description'},
                         headers = my_headers)
    new_body = resp.json()
    company_id = new_body['id']

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)

    assert resp.status_code == status_code

    employee_api.delete_company(company_id) 


def test_add_employee_without_company_id():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "firstName" : "Employee",
        "lastName" : "Employee",
        "middleName" : "Employee",
        "phone" : "+79123456789",
        "url" : "url"
    }

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_add_employee_without_first_name():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "lastName" : "Employee",
        "middleName" : "Employee",
        "phone" : "+79123456789",
        "url" : "url"
    }

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_add_employee_without_last_name():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "Employee",
        "middleName" : "Employee",
        "phone" : "+79123456789",
        "url" : "url"
    }

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_add_employee_without_middle_name():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "Employee",
        "lastName" : "Employee",
        "phone" : "+79123456789",
        "url" : "url"
    }

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_add_employee_without_phone():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "Employee",
        "lastName" : "Employee",
        "middleName" : "Employee",
        "url" : "url"
    }

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_add_employee_without_url():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId": company_id,
        "firstName": "Employee",
        "lastName": "Employee",
        "middleName": "Employee",
        "phone": "+79123456789"
    }

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_add_new_employee_without_fields():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {}

    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    assert resp.status_code == 400

    employee_api.delete_company(company_id)


@pytest.mark.parametrize("change_employee, status_code",
    [
    ({'lastName': None, 'email': 'email', 'url': 'url', 'isActive': True}, 400),
    ({'lastName': 'lastName', 'email': None, 'url': 'url', 'isActive': True}, 400),
    ({'lastName': 'lastName', 'email': 'email', 'url': None, 'isActive': True}, 400),
    ({'lastName': 'lastName', 'email': 'email', 'url': None, 'isActive': False}, 400),    
    ({'lastName': 'lastName', 'email': 'email', 'url': 'url', 'isActive': None}, 400)
    ])
def test_change_employees(change_employee, status_code):
    employee_api = Employee(base_url)
    creds = { 
        'username' : 'roxy',
        'password' : 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token

    new_company = requests.post(base_url + "/company", json={'name': 'Company For Employees', 'description': 'Description'},
                         headers = my_headers)
    new_body = new_company.json()
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "first_name",
        "lastName" : "last_name",
        "middleName" : "middle_name",
        "phone" : "phone",
        "url" : "url"
    }

    new_employee = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    new_body = new_employee.json()
    new_employee_id = new_body['id']

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)

    assert resp.status_code == status_code

    employee_api.delete_company(company_id)

def test_change_employee_without_last_name():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "first_name",
        "lastName" : "last_name",
        "middleName" : "middle_name",
        "phone" : "phone",
        "url" : "url"
    }

    new_employee = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    new_body = new_employee.json()
    new_employee_id = new_body['id']

    change_employee = {
        "email": "new_email",
        "url" : "new_url",
        "isActive" : True
    }

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)

    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_change_employee_without_email():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "first_name",
        "lastName" : "last_name",
        "middleName" : "middle_name",
        "phone" : "phone",
        "url" : "url"
    }

    new_employee = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    new_body = new_employee.json()
    new_employee_id = new_body['id']

    change_employee = {
        "lastName" : "lastName",
        "url" : "new_url",
        "isActive" : True
    }

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)

    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_change_employee_without_url():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "first_name",
        "lastName" : "last_name",
        "middleName" : "middle_name",
        "phone" : "phone",
        "url" : "url"
    }

    new_employee = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    new_body = new_employee.json()
    new_employee_id = new_body['id']

    change_employee = {
        "lastName" : "lastName",
        "email": "new_email",
        "isActive" : True
    }

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)

    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_change_employee_without_is_active():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "first_name",
        "lastName" : "last_name",
        "middleName" : "middle_name",
        "phone" : "phone",
        "url" : "url"
    }

    new_employee = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    new_body = new_employee.json()
    new_employee_id = new_body['id']

    change_employee = {
        "lastName" : "lastName",
        "email": "new_email",
        "url" : "new_url"
    }

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)

    assert resp.status_code == 400

    employee_api.delete_company(company_id)


def test_change_employee_without_fields():
    employee_api = Employee(base_url)
    creds = { 
        'username': 'roxy',
        'password': 'animal-fairy'
    }

    resp = requests.post(base_url + "/auth/login", json=creds)
    token =  resp.json()["userToken"]

    my_headers = {}
    my_headers['x-client-token'] = token
    
    name = 'Компания для сотрудников'
    description = 'Проверка обязательности полей'
    new_body = employee_api.add_new_company(name, description)
    company_id = new_body['id']

    new_employee = {
        "companyId" : company_id,
        "firstName" : "first_name",
        "lastName" : "last_name",
        "middleName" : "middle_name",
        "phone" : "phone",
        "url" : "url"
    }

    new_employee = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    new_body = new_employee.json()
    new_employee_id = new_body['id']

    change_employee = {}

    resp = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)

    assert resp.status_code == 400

    employee_api.delete_company(company_id)