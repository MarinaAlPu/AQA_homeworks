import allure
from sqlalchemy import create_engine
from sqlalchemy.sql import text
from faker import Faker
fake = Faker()
fake_ru = Faker("ru_RU")

class EmployeeTable:
    __my_scripts = {
        "insert new company": text("insert into company (\"name\", \"description\") values (:new_name, :new_description)"),
        "select company list": text("select * from company"),
        "get max company id": text("select MAX(id) from company"),
        "insert new employee": text("insert into employee (\"first_name\", \"last_name\", \"middle_name\", \
                                    \"phone\", \"avatar_url\", \"companyId\") values (:first_name, \
                                    :last_name, :middle_name, :phone, :url, :company_id)"),
        "get employee list by company id": text("select * from employee where \"companyId\" = :company_id"),
        "delete company by id": text("delete from company where id = :id_to_delete"),
        "delete employee by id": text("delete from employee where \"companyId\" = :id_to_delete"),
        "get employee by id": text("select * from employee where id = :employee_id and \"companyId\" = :company_id"),
        "get max employee id": text("select MAX(id) from employee where \"companyId\" = :company_id"),
        "update employee by id": text("update employee set \"last_name\" = :updated_last_name, \
                                      \"email\" = :updated_email, \"avatar_url\" = avatar_url, \
                                      \"isActive\" = true where \"id\" = ':employee_id' and \
                                      \"companyId\" = ':company_id'")
    }

    def __init__(self, connection_string: str):
        self.__db = create_engine(connection_string)

    @allure.step("БД. Получить список компаний")
    def get_company_list(self) -> list:
        query = self.__db.execute(self.__my_scripts["select company list"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()    

    @allure.step("БД. Создать компанию")
    def add_company(self) -> dict:
        query = self.__db.execute(self.__my_scripts["insert new company"],
                                 new_name = fake.company(),
                                 new_description = fake.text())
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query

    @allure.step("БД. Получить id созданной компании")
    def get_max_company_id(self) -> int:
        query = self.__db.execute(self.__my_scripts["get max company id"])
        allure.attach(str(query.context.cursor.query), 'SQL', allure.attachment_type.TEXT)
        return query.fetchall()[0][0]

    def format_numbers(self, phone_number: str) -> str:
        """
        Форматирует сгенерированный номер телефона: приводит к виду +7ХХХХХХХХХХ.
        """
        phone_number = fake_ru.phone_number()
        return '+7{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}'.format(*[i for i in phone_number if i.isdigit()][1:])

    @allure.step("БД. Добавить сотрудника в компанию {id}")
    def add_employee(self, id: int) -> dict:
        with allure.step("Сгенерировать данные для создания сотрудника."):
            with allure.step("БД. Добавить сотрудника в компанию"):        
                return self.__db.execute(self.__my_scripts["insert new employee"],\
                                        first_name = fake_ru.first_name(), last_name = fake_ru.last_name(),\
                                        middle_name = fake_ru.middle_name(),\
                                        phone = self.format_numbers(fake_ru.phone_number()),\
                                        url = fake.url(), company_id = id)

    @allure.step("БД. Получить информацию о сотруднике {new_employee_id}")
    def get_employee_from_db(self, new_employee_id: int, id: int) -> dict:
        return self.__db.execute(self.__my_scripts["get employee by id"], employee_id = new_employee_id, company_id = id).fetchall() 

    @allure.step("БД. Получить список сотрудников компании {id}")
    def get_employee_list(self, id: int) -> list:
        return self.__db.execute(self.__my_scripts["get employee list by company id"], company_id = id).fetchall()  

    @allure.step("БД. Удалить компанию {id}")
    def delete_company(self, id: int) -> dict:
        self.__db.execute(self.__my_scripts["delete company by id"], id_to_delete = id)

    @allure.step("БД. Удалить сотрудников компании {id}")
    def delete_employee_by_company_id(self, id: int) -> dict:
        self.__db.execute(self.__my_scripts["delete employee by id"], id_to_delete = id)        

    @allure.step("БД. Получить id добавленного сотрудника")
    def get_max_employee_id(self, id: int) -> int:
        return self.__db.execute(self.__my_scripts["get max employee id"], company_id = id).fetchall()[0][0]

    @allure.step("БД. Изменить информацию о сотруднике {employee_id}")
    def update_employee(self, employee_id: int, id: int) -> dict:
        self.__db.execute(self.__my_scripts["update employee by id"],\
                          updated_last_name = fake_ru.last_name(),\
                          updated_email = fake.email(), updated_url = fake.url(),\
                          employee_id = employee_id, company_id = id)
