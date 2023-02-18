import requests

base_url = "https://x-clients-be.onrender.com"

def test_get_company():
    resp = requests.get(base_url + '/company')

    response_body = resp.json()

    my_company = response_body[2]

    assert my_company["name"] == "Клининг-центр 'Клинг-кинг'"
    assert resp.status_code == 200
    assert resp.headers["Content-Type"] == "application/json; charset=utf-8"

    my_id = response_body[2]["id"]
    assert my_id == 3

def test_get_employee():
    creds = { 
        'username':'roxy',
        'password': 'animal-fairy'
    }
    resp = requests.get(base_url + '/company')

    response_body = resp.json()

    #my_company = response_body[2]

    employee = { 
        'id': response_body[2]["id"]
    }

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]   

    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.get(base_url + '/employee?company=3', json=employee, headers = my_headers)
    assert resp.status_code == 200

    response_body = resp.json()
    assert len(response_body) > 0
    print(len(response_body))

def test_new_employee():
    creds = { 
        'username':'roxy',
        'password': 'animal-fairy'
    }

    new_employee = {
        'companyId': 3,
        'firstName': 'Ivan',
        'lastName': 'Ivanov',
        'middleName': 'Ivanych',
        'phone': '+79123456789',
        'url': 'string'
    }

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]   

    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.post(base_url + '/employee', json=new_employee, headers = my_headers)
    assert resp.status_code == 201

    my_employee_id = resp.json()
    print(my_employee_id)


def test_get_updated_employee():
    creds = { 
        'username':'roxy',
        'password': 'animal-fairy'
    }

    employee = { 
        'id': 3
    }

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]   

    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.get(base_url + '/employee?company=3', json=employee, headers = my_headers)
    response_body = resp.json()
    assert len(response_body) > 0
    print(len(response_body))
    
    assert resp.status_code == 200

def test_get_info_employee_by_id():
    resp = requests.get(base_url + '/employee/17')
    assert resp.status_code == 200

    response_body = resp.json()
    my_employee_first_name = response_body["first_name"]
    print(my_employee_first_name)

def test_change_employee():
    creds = { 
        'username':'roxy',
        'password': 'animal-fairy'
    }

    change_employee = {
        'lastName': 'Petrov',
        'email': '123@test.ru',
        'url': 'some url',
        'isActive': True
    }

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]   

    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.patch(base_url + '/employee/7', json=change_employee, headers = my_headers)
    assert resp.status_code == 200

def test_get_updated_info_employee():
    resp = requests.get(base_url + '/employee/7')
    assert resp.status_code == 200

    response_body = resp.json()
    my_employee_last_name = response_body["last_name"]
    my_employee_email = response_body["email"]
    my_employee_url = response_body["avatar_url"]
    my_employee_is_active = response_body["isActive"]

    print(my_employee_last_name)
    print(my_employee_email)
    print(my_employee_url)
    print(my_employee_is_active)

    assert my_employee_last_name == "Petrov"
    assert my_employee_email == "123@test.ru"
    assert my_employee_url == "some url"
    assert my_employee_is_active == True