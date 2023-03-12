import allure
import requests
from faker import Faker
fake = Faker()
fake_ru = Faker("ru_RU")

class Employee:
    def __init__(self, url: str):
        self.url = url

    @allure.step("API. Получить список компаний")
    def get_company_list(self) -> list:
        resp = requests.get(self.url + '/company')
        return resp.json()
    
    @allure.step("API. Получить список сотрудников компании {id}")
    def get_employee_list(self, id: int) -> list:
        resp = requests.get(self.url + '/employee?company=' + str(id))        
        return resp.json()
    
    @allure.step("API. Получить токен авторизации для пользователя {user}: {password}")
    def get_token(self, user = 'roxy', password = 'animal-fairy') -> str:
        creds = { 
        'username' : user,
        'password' : password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
  
    @allure.step("API. Создать компанию {name} ({description})")  
    def add_new_company(self) -> dict:
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        new_company = {
            'name' : fake.company(),
            'description' : fake.text()
        }   

        resp = requests.post(self.url + '/company', json=new_company, headers = my_headers)
        return resp.json()        

    @allure.step("API. Создать сотрудника в компании {company_id}")
    def add_new_employee(self, company_id: int, first_name: str, last_name: str, middle_name: str, phone: str, url: str) -> dict:
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()        

        with allure.step("Сгенерировать данные для создания сотрудника."):        
            new_employee = {
                "companyId" : company_id,
                "firstName" : first_name,
                "lastName" : last_name,
                "middleName" : middle_name,
                "phone" : phone,
                "url" : url
            }

        resp = requests.post(self.url + '/employee', json=new_employee, headers = my_headers)
        return resp.json()

    def format_numbers(self, phone_number: str) -> str:
        """
        Форматирует сгенерированный номер телефона: приводит к виду +7ХХХХХХХХХХ.
        """
        phone_number = fake_ru.phone_number()
        return '+7{0}{1}{2}{3}{4}{5}{6}{7}{8}{9}'.format(*[i for i in phone_number if i.isdigit()][1:])

    @allure.step("API. Получить информацию о сотруднике {id}")
    def get_employee_info(self, id: int) -> dict:
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()        

    @allure.step("API. Удалить компанию {id}")
    def delete_company(self, id: int) -> dict:
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers = my_headers)
        return resp.json()

    @allure.step("API. Изменить информацию о сотруднике {id}")
    def change_employee_info(self, id: int, new_last_name, new_email, new_url, new_is_active: bool) -> dict:
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()        
        
        new_employee = {
            "lastName" : new_last_name,
            "email": new_email,
            "url" : new_url,
            "isActive" : new_is_active
        }

        resp = requests.patch(self.url + '/employee/' + str(id), json = new_employee, headers = my_headers)
        return resp.json()