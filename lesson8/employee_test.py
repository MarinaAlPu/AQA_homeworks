import pytest
import requests
from newEmployeeApi import Employee

base_url = "https://x-clients-be.onrender.com"

def test_get_employee_list():
    employee_api = Employee(base_url)
    new_body = employee_api.add_new_company()
    new_company_id = new_body['id']    
    employee_api.add_new_employee_without_company(new_company_id)
    employee_list = employee_api.get_employee_list(new_company_id)
    employee_api.delete_company(new_company_id)    
    assert len(employee_list) > 0
    

def test_add_new_employee():
    employee_api = Employee(base_url)
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

    new_body = employee_api.add_new_company()
    new_company_id = new_body['id']

    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)
    assert len_after - len_before == 1
    assert company_list_after[-1]["id"] == new_company_id

    employee_body_before = employee_api.get_employee_list(new_company_id)
    staff_before = len(employee_body_before)

    company_id = new_company_id
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanych"
    phone = "79123456789"
    url = "his url"
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

    employee_body_after = employee_api.get_employee_list(new_company_id)
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

    company_list_end = employee_api.get_company_list()
    len_end = len(company_list_end)
    assert len_before == len_end
    assert company_list_end[-1]["id"] != new_company_id


def test_get_employee_by_id():
    employee_api = Employee(base_url)
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

    new_body = employee_api.add_new_company()
    new_company_id = new_body['id']

    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)
    assert len_after - len_before == 1
    assert company_list_after[-1]["id"] == new_company_id

    employee_body_before = employee_api.get_employee_list(new_company_id)
    staff_before = len(employee_body_before)

    company_id = new_company_id
    first_name = "Ivan"
    last_name = "Ivanov"
    middle_name = "Ivanych"
    phone = "79123456789"
    url = "Какой-то url"
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

    employee_body_after = employee_api.get_employee_list(new_company_id)
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

    company_list_end = employee_api.get_company_list()
    len_end = len(company_list_end)
    assert len_before == len_end
    assert company_list_end[-1]["id"] != id


def test_change_info_employee():
    employee_api = Employee(base_url)
    company_list_before = employee_api.get_company_list()
    len_before = len(company_list_before)

    new_body = employee_api.add_new_company()
    new_company_id = new_body['id']

    company_list_after = employee_api.get_company_list()
    len_after = len(company_list_after)
    assert len_after - len_before == 1
    assert company_list_after[-1]["id"] == new_company_id

    employee_body_before = employee_api.get_employee_list(new_company_id)
    staff_before = len(employee_body_before)

    new_employee_body = employee_api.add_new_employee_without_company(new_company_id)
    new_employee_id = new_employee_body['id']

    employee_body_after = employee_api.get_employee_list(new_company_id)
    staff_after = len(employee_body_after)
    assert staff_after - staff_before == 1

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
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'first_name': 'first Name', 'last_name': 'last Name',
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'last_name': 'last Name',
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 
      'middle_name': 'middle Name', 'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': 'last Name', 
      'phone': '+79123456789', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'url': 'некий url'}, 400),

    ({'company_id': 'company_id', 'first_name': 'first Name', 'last_name': 'last Name', 
      'middle_name': 'middle Name', 'phone': '+79123456789', }, 400),    

    ({}, 400)
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

    new_body = employee_api.add_new_company()
    company_id = new_body['id']
    1 == 1
    resp = requests.post(base_url + "/employee", json=new_employee, headers = my_headers)
    1 == 1
    employee_api.delete_company(company_id) 
    1 == 1
    assert resp.status_code == status_code


@pytest.mark.parametrize("change_employee, status_code",
    [
    ({'lastName': None, 'email': 'new@email.test', 'url': 'new url', 'isActive': True}, 400),
    ({'lastName': 'New Last Name', 'email': None, 'url': 'new url', 'isActive': True}, 400),
    ({'lastName': 'New Last Name', 'email': 'new@email.test', 'url': None, 'isActive': True}, 400),
    ({'lastName': 'New Last Name', 'email': 'new@email.test', 'url': 'new url', 'isActive': False}, 400),    
    ({'lastName': 'New Last Name', 'email': 'new@email.test', 'url': 'new url', 'isActive': None}, 400),
    ({'email': 'new@email.test', 'url' : 'new url', 'isActive' : True}, 400),
    ({'lastName' : 'New Last Name', 'url' : 'new url', 'isActive' : True}, 400),
    ({'lastName': 'New Last Name', 'email': 'new@email.test', 'isActive': True}, 400),   
    ({'lastName': 'New Last Name', 'email': 'new@email.test', 'url': 'new url'}, 400),
    ({}, 400)
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

    new_body = employee_api.add_new_company()
    company_id = new_body['id']
    
    new_employee = employee_api.add_new_employee_without_company(company_id)
    new_employee_id = new_employee['id']

    changed_employee = requests.patch(base_url + '/employee/' + str(new_employee_id), json = change_employee, headers = my_headers)
    
    employee_api.delete_company(company_id)

    assert changed_employee.status_code == status_code
