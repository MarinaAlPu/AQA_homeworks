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
                                    \"phone\", \"email\", \"avatar_url\", \"companyId\") values (:first_name, \
                                    :last_name, :middle_name, :phone, :email, :url, :company_id)"),
        "get employee list by company id": text("select * from employee where \"companyId\" = :company_id"),
        "delete company by id": text("delete from company where id = :id_to_delete"),
        "delete employee by id": text("delete from employee where \"companyId\" = :id_to_delete"),
        "get employee by id": text("select * from employee where id = :employee_id and \"companyId\" = :company_id"),
        "get max employee id": text("select MAX(id) from employee where \"companyId\" = :company_id"),
        "update employee by id": text("update employee set \"last_name\" = ':updated_last_name', \
                                      \"email\" = ':updated_email', \"avatar_url\" = 'updated_url', \
                                      \"isActive\" = true where \"id\" = ':employee_id' and \
                                      \"companyId\" = ':company_id'")
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def get_company_list(self):
        return self.__db.execute(self.__my_scripts["select company list"]).fetchall()       

    def add_company(self):
        return self.__db.execute(self.__my_scripts["insert new company"],
                                 new_name = fake.company(),
                                 new_description = fake.text())

    def get_max_company_id(self):
        return self.__db.execute(self.__my_scripts["get max company id"]).fetchall()[0][0]
    
    def add_employee(self, id):
        return self.__db.execute(self.__my_scripts["insert new employee"],\
                                 first_name = fake_ru.first_name(), last_name = fake_ru.last_name(),\
                                 middle_name = fake_ru.middle_name(), phone = fake.phone_number(),\
                                 email = fake.email(), url = fake.url(), company_id = id)

    def get_employee_from_db(self, new_employee_id, id):
        return self.__db.execute(self.__my_scripts["get employee by id"], employee_id = new_employee_id, company_id = id).fetchall() 

    def get_employee_list(self, id):
        return self.__db.execute(self.__my_scripts["get employee list by company id"], company_id = id).fetchall()  

    def delete_company(self, id):
        self.__db.execute(self.__my_scripts["delete company by id"], id_to_delete = id)

    def delete_employee_by_company_id(self, id):
        self.__db.execute(self.__my_scripts["delete employee by id"], id_to_delete = id)        

    def get_max_employee_id(self, id):
        return self.__db.execute(self.__my_scripts["get max employee id"], company_id = id).fetchall()[0][0]
    
    def update_employee(self, employee_id, id):
        self.__db.execute(self.__my_scripts["update employee by id"],\
                          updated_last_name = fake.last_name(),\
                          updated_email = fake.email(), updated_url = fake.url(),\
                          employee_id = employee_id, company_id = id)

        