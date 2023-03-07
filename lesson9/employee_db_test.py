from EmployeeApi import Employee
from EmployeeTable import EmployeeTable
from faker import Faker
fake = Faker()
fake_ru = Faker("ru_RU")

base_url = "https://x-clients-be.onrender.com"
employee_api = Employee(base_url)

db = EmployeeTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")

# def test_get_employee_list():
#     employee_api = Employee(base_url)

#     db.add_company()
#     max_company_id = db.get_max_company_id()

#     for x in range(0, 3):
#         db.add_employee(max_company_id)

#     list_employee_api = employee_api.get_employee_list(max_company_id)
#     list_employee_db = db.get_employee_list(max_company_id)

#     db.delete_employee_by_company_id(max_company_id)
#     db.delete_company(max_company_id)

#     assert len(list_employee_api) == len(list_employee_db)

    
def test_add_new_employee():
    employee_api = Employee(base_url)

    db.add_company()
    max_company_id = db.get_max_company_id()

    company_id = max_company_id
    first_name = fake_ru.first_name()
    last_name = fake_ru.last_name()
    middle_name = fake_ru.middle_name()
    phone = db.format_numbers(fake_ru.phone_number())
    url = fake.url()
    new_employee_body = employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
    new_employee_id = new_employee_body['id']

    employee_from_db = db.get_employee_from_db(new_employee_id, max_company_id)
    employee = employee_from_db[0]
    assert employee[0] == new_employee_id
    assert employee["first_name"] == first_name
    assert employee["last_name"] == last_name
    assert employee["middle_name"] == middle_name
    assert employee["phone"] == phone
    assert employee["avatar_url"] == url

    db.delete_employee_by_company_id(max_company_id)
    db.delete_company(max_company_id)
    

# def test_get_employee_by_id():
#     employee_api = Employee(base_url)

#     db.add_company()
#     max_company_id = db.get_max_company_id()

#     db.add_employee(max_company_id)
#     max_employee_id = db.get_max_employee_id(max_company_id)
  
#     employee_from_db = db.get_employee_from_db(max_employee_id, max_company_id)
#     employee = employee_from_db[0]  

#     body = employee_api.get_employee_info(max_employee_id)

#     assert body["companyId"] == employee["companyId"]
#     assert body["firstName"] == employee["first_name"]
#     assert body["lastName"] == employee["last_name"]
#     assert body["middleName"] == employee["middle_name"]
#     assert body["phone"] == employee["phone"]
#     assert body["avatar_url"] == employee["avatar_url"]

#     db.delete_employee_by_company_id(max_company_id)
#     db.delete_company(max_company_id)


# def test_change_info_employee():
#     employee_api = Employee(base_url)

#     db.add_company()
#     max_company_id = db.get_max_company_id()

#     db.add_employee(max_company_id)
#     max_employee_id = db.get_max_employee_id(max_company_id)

#     new_last_name = fake_ru.last_name()
#     new_email = fake_ru.email()
#     new_url = fake_ru.url()
#     new_is_active = True
#     employee_api.change_employee_info(max_employee_id, new_last_name, new_email, new_url, new_is_active)

#     employee_from_db = db.get_employee_from_db(max_employee_id, max_company_id)
#     employee = employee_from_db[0] 

#     assert employee["isActive"] == new_is_active
#     assert employee["id"] == max_employee_id
#     assert employee["email"] == new_email
#     assert employee["avatar_url"] == new_url

#     db.delete_employee_by_company_id(max_company_id)
#     db.delete_company(max_company_id)

# def test_change_employee_in_db():
#     employee_api = Employee(base_url)

#     db.add_company()
#     max_company_id = db.get_max_company_id()

#     db.add_employee(max_company_id)
#     max_employee_id = db.get_max_employee_id(max_company_id)

#     db.update_employee(max_employee_id, max_company_id)

#     body = employee_api.get_employee_info(max_employee_id)

#     employee_from_db = db.get_employee_from_db(max_employee_id, max_company_id)
#     employee = employee_from_db[0] 

#     assert body["companyId"] == employee["companyId"]
#     assert body["lastName"] == employee["last_name"]
#     assert body["isActive"] == employee["isActive"]
#     assert body["email"] == employee["email"]
#     assert body["avatar_url"] == employee["avatar_url"]

#     db.delete_employee_by_company_id(max_company_id)
#     db.delete_company(max_company_id)