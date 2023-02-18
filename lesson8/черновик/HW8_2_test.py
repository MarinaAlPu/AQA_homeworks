import requests

base_url = "https://x-clients-be.onrender.com"
company_id_for_url = 0
my_employee_id = 0
id_for_search = 0

def test_get_employee():
    creds = { 
        'username':'roxy',
        'password': 'animal-fairy'
    }

    # global company_id_for_url
    # global my_employee_id
    # global id_for_search

    resp = requests.get(base_url + '/company')
    response_body = resp.json()
    print("Количество компаний:", len(response_body))

    #response_body = resp.json()
    
    company_id_for_url = response_body[2]["id"]

    resp = requests.post(base_url + '/auth/login', json=creds)
    token = resp.json()["userToken"]   

    my_headers = {}
    my_headers['x-client-token'] = token

    resp = requests.get(base_url + '/employee?company=' + 'company_id_for_url', headers = my_headers)
    response_body = resp.json()
    print("Количество сотрудников в компании:", len(response_body))
    assert resp.status_code == 200

    new_employee = {
        'companyId': company_id_for_url,
        'firstName': 'Ivan',
        'lastName': 'Ivanov',
        'middleName': 'Ivanych',
        'phone': '+79123456789',
        'url': 'string'
    }

    resp_id = requests.post(base_url + '/employee', json=new_employee, headers = my_headers)
    assert resp_id.status_code == 201

    my_employee_id = resp_id.json()
    print(my_employee_id)

    id_for_search = my_employee_id["id"]
    print("id нового сотрудника:", id_for_search) # для получения сотрудника по id

    resp = requests.get(base_url + '/employee?company=' + 'company_id_for_url', headers = my_headers)
    response_body = resp.json()
    print("Новое количество сотрудников", len(response_body))
    
    assert resp.status_code == 200

# получить сотрудника по id
    resp = requests.get(base_url + '/employee/2')  #'+'id_for_search
    assert resp.status_code == 200

    print("Данные сотрудника до изменений")
    response_body = resp.json()
    my_employee_last_name = response_body["last_name"]
    my_employee_email = response_body["email"]
    my_employee_url = response_body["avatar_url"]
    my_employee_is_active = response_body["isActive"]
    
    print(my_employee_last_name)
    print(my_employee_email)
    print(my_employee_url)
    print(my_employee_is_active)

    change_employee = {
        'lastName': 'Petrov',
        'email': '123@test.ru',
        'url': 'some url',
        'isActive': True
    }

    resp = requests.patch(base_url + '/employee/2', json=change_employee, headers = my_headers)
    assert resp.status_code == 200

    resp = requests.get(base_url + '/employee/2')
    assert resp.status_code == 200
    print("Данные сотрудника после изменений:")

    response_body = resp.json()
    my_employee_last_name1 = response_body["last_name"]
    my_employee_email1 = response_body["email"]
    my_employee_url1 = response_body["avatar_url"]
    my_employee_is_active1 = response_body["isActive"]

    print(my_employee_last_name1)
    print(my_employee_email1)
    print(my_employee_url1)
    print(my_employee_is_active1)

    assert my_employee_last_name1 == my_employee_last_name
    assert my_employee_email1 == my_employee_email
    assert my_employee_url1 == my_employee_url
    assert my_employee_is_active1 == True