import pytest
import allure
from EmployeeApi import Employee
from EmployeeTable import EmployeeTable
from random import randint
from faker import Faker
fake = Faker()
fake_ru = Faker("ru_RU")

@allure.epic("Сотрудники")
@allure.suite("Тестирование операций с сотрудниками")
class EmployeeTest:
    base_url = "https://x-clients-be.onrender.com"
    db = EmployeeTable("postgresql://x_clients_user:SZIgROntPcmlRYoaICpxIHbLwjMx43Pm@dpg-cfadlr1gp3jsh6etrpu0-a.frankfurt-postgres.render.com/xclients")

    @allure.story("Поучение информации о сотрудниках")
    @allure.title("Получение полного списка всех сотрудников одной компании")
    @allure.description("Проверка работы GET-запроса на получение полного списка\
                        сотрудников одной компании по id компании")
    @allure.feature("GET")
    @allure.severity("critical")
    @allure.id("E-1")
    def test_get_employee_list(self):
        with allure.step("Создать экземпляр класса Employee."):
            self.employee_api = Employee(self.base_url)

        self.db.add_company()
        max_company_id = self.db.get_max_company_id()

        with allure.step("Добавить сотрудников в созданную компанию {max_company_id}."):
            for x in range(0, randint(1, 5)):
                self.db.add_employee(max_company_id)

        list_employee_api = self.employee_api.get_employee_list(max_company_id)
        list_employee_db = self.db.get_employee_list(max_company_id)

        with allure.step("Проверить, что количество сотрудников, полученное через API,\
                        и количество сотрудников, полученное из БД, совпадают."):
            assert len(list_employee_api) == len(list_employee_db)

        self.db.delete_employee_by_company_id(max_company_id)
        self.db.delete_company(max_company_id)

    @allure.story("Создание сотрудников")
    @allure.title("Создание сотрудника в компании по id компании")
    @allure.description("Проверка работы POST-запроса на добавление сотрудника в компанию")
    @allure.feature("CREATE")
    @allure.severity("critical")
    @allure.id("E-2")    
    def test_add_new_employee(self):
        with allure.step("Создать экземпляр класса Employee."):
            self.employee_api = Employee(self.base_url)

        self.db.add_company()
        max_company_id = self.db.get_max_company_id()

        company_id = max_company_id
        first_name = fake_ru.first_name()
        last_name = fake_ru.last_name()
        middle_name = fake_ru.middle_name()
        phone = self.employee_api.format_numbers(fake_ru.phone_number())
        url = fake.url()

        new_employee_body = self.employee_api.add_new_employee(company_id, first_name, last_name, middle_name, phone, url)
        
        with allure.step("Получить id нового сотрудника."):
            new_employee_id = new_employee_body['id']

        employee_from_db = self.db.get_employee_from_db(new_employee_id, max_company_id)
        employee = employee_from_db[0]

        with allure.step("Проверить, что данные сотрудника, полученные из БД,\
                        и данные, сгенерированные для создания сотрудника, совпадают."):
            assert employee[0] == new_employee_id
            assert employee["first_name"] == first_name
            assert employee["last_name"] == last_name
            assert employee["middle_name"] == middle_name
            assert employee["phone"] == phone
            assert employee["avatar_url"] == url

        self.db.delete_employee_by_company_id(max_company_id)
        self.db.delete_company(max_company_id)

    @allure.story("Поучение информации о сотрудниках")
    @allure.title("Получение информации об одном сотруднике компании")
    @allure.description("Проверка работы GET-запроса на получение информации о сотруднике компании по id сотрудника")
    @allure.feature("GET")
    @allure.severity("critical")        
    @allure.id("E-3")
    def test_get_employee_by_id(self):
        with allure.step("Создать экземпляр класса Employee."):
            self.employee_api = Employee(self.base_url)

        self.db.add_company()
        max_company_id = self.db.get_max_company_id()

        self.db.add_employee(max_company_id)

        max_employee_id = self.db.get_max_employee_id(max_company_id)
    
        employee_from_db = self.db.get_employee_from_db(max_employee_id, max_company_id)
        employee = employee_from_db[0]  

        body = self.employee_api.get_employee_info(max_employee_id)

        with allure.step("Проверить, что данные сотрудника, полученные через API,\
                        и данные сотрудника, полученные из БД, совпадают."):
            assert body["companyId"] == employee["companyId"]
            assert body["firstName"] == employee["first_name"]
            assert body["lastName"] == employee["last_name"]
            assert body["middleName"] == employee["middle_name"]
            assert body["phone"] == employee["phone"]
            assert body["avatar_url"] == employee["avatar_url"]

        self.db.delete_employee_by_company_id(max_company_id)
        self.db.delete_company(max_company_id)

    @allure.story("Изменение информации о сотрудниках")
    @allure.title("Изменение информации о сотруднике через API")
    @allure.description("Проверка работы PATCH-запроса на изменение информации о сотруднике по id сотрудника")
    @allure.feature("UPDATE")
    @allure.severity("critical")
    @allure.id("E-4")
    def test_change_info_employee(self):
        with allure.step("Создать экземпляр класса Employee."):
            self.employee_api = Employee(self.base_url)

        self.db.add_company()
        max_company_id = self.db.get_max_company_id()

        self.db.add_employee(max_company_id)
        max_employee_id = self.db.get_max_employee_id(max_company_id)

        with allure.step("Сгенерировать данные для изменения информации о сотруднике."):
            new_last_name = fake_ru.last_name()
            new_email = fake_ru.email()
            new_url = fake_ru.url()
            new_is_active = True

        self.employee_api.change_employee_info(max_employee_id, new_last_name, new_email, new_url, new_is_active)

        employee_from_db = self.db.get_employee_from_db(max_employee_id, max_company_id)
        employee = employee_from_db[0] 

        with allure.step("Проверить, что данные сотрудника, полученные из БД,\
                        и данные, сгенерированные для изменения информации о сотруднике, совпадают."):
            assert employee["isActive"] == new_is_active
            assert employee["id"] == max_employee_id
            assert employee["email"] == new_email
            assert employee["avatar_url"] == new_url

        self.db.delete_employee_by_company_id(max_company_id)
        self.db.delete_company(max_company_id)