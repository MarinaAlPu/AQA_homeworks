import requests
import random

class Employee:
    def __init__(self, url):
        self.url = url

    def get_company_list(self):
        resp = requests.get(self.url + '/company')
        return resp.json()
    
    def get_employee_list(self, id):
        resp = requests.get(self.url + '/employee?company=' + str(id))        
        return resp.json()
    
    def get_token(self, user = 'roxy', password = 'animal-fairy'):
        creds = { 
        'username' : user,
        'password' : password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]
    
    def add_new_company(self):
        name_list = ["Company 1", "Company 2", "Company 3", "Company 4", "Company 5"]
        description_list = ["Description 1", "Description 2", "Description 3", "Description 4", "Description 5"]

        random_name_index = random.randint(0, len(name_list) - 1)
        random_description_index = random.randint(0, len(description_list) - 1)

        new_company = {
            'name' : name_list[random_name_index],
            'description' : description_list[random_description_index]
        }

        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        resp = requests.post(self.url + '/company', json=new_company, headers = my_headers)
        return resp.json()

    def add_new_employee(self, company_id, first_name, last_name, middle_name, phone, url):
        new_employee = {
            "companyId" : company_id,
            "firstName" : first_name,
            "lastName" : last_name,
            "middleName" : middle_name,
            "phone" : phone,
            "url" : url
        }
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.post(self.url + '/employee', json=new_employee, headers = my_headers)
        return resp.json()

    def add_new_employee_without_company(self, id):
        employees = [
            {"companyId" : id, "firstName" : "First name 1","lastName" : "Last name 1",
            "middleName" : "Middle name 1", "phone" : "+79111111111", "url" : "url 1"},

            {"companyId" : id, "firstName" : "First name 2","lastName" : "Last name 2",
            "middleName" : "Middle name 2", "phone" : "+79222222222", "url" : "url 2"},

            {"companyId" : id, "firstName" : "First name 3","lastName" : "Last name 3",
            "middleName" : "Middle name 3", "phone" : "+79333333333", "url" : "url 3"},

            {"companyId" : id, "firstName" : "First name 4","lastName" : "Last name 4",
            "middleName" : "Middle name 4", "phone" : "+79444444444", "url" : "url 4"},

            {"companyId" : id, "firstName" : "First name 5","lastName" : "Last name 5",
            "middleName" : "Middle name 5", "phone" : "+79555555555", "url" : "url 5"}            
        ]

        random_employee_index = random.randint(0, len(employees) - 1)

        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        resp = requests.post(self.url + '/employee', json=employees[random_employee_index], headers = my_headers)
        return resp.json()

    def add_new_employee_with_company(self):
        new_body = self.add_new_company()
        new_company_id = new_body['id']

        employees = [
            {"companyId" : new_company_id, "firstName" : "First name 1","lastName" : "Last name 1",
            "middleName" : "Middle name 1", "phone" : "+79111111111", "url" : "url 1"},

            {"companyId" : new_company_id, "firstName" : "First name 2","lastName" : "Last name 2",
            "middleName" : "Middle name 2", "phone" : "+79222222222", "url" : "url 2"},

            {"companyId" : new_company_id, "firstName" : "First name 3","lastName" : "Last name 3",
            "middleName" : "Middle name 3", "phone" : "+79333333333", "url" : "url 3"},

            {"companyId" : new_company_id, "firstName" : "First name 4","lastName" : "Last name 4",
            "middleName" : "Middle name 4", "phone" : "+79444444444", "url" : "url 4"},

            {"companyId" : new_company_id, "firstName" : "First name 5","lastName" : "Last name 5",
            "middleName" : "Middle name 5", "phone" : "+79555555555", "url" : "url 5"}            
        ]

        random_employee_index = random.randint(0, len(employees) - 1)

        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        resp = requests.post(self.url + '/employee', json=employees[random_employee_index], headers = my_headers)
        return resp.json()

    def get_employee_info(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return resp.json()        

    def delete_company(self, id):
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()
        resp = requests.get(self.url + '/company/delete/' + str(id), headers = my_headers)
        return resp.json()

    def change_employee_info(self, id, new_last_name, new_email, new_url, new_is_active):
        new_employee = {
            "lastName" : new_last_name,
            "email": new_email,
            "url" : new_url,
            "isActive" : new_is_active
        }

        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        resp = requests.patch(self.url + '/employee/' + str(id), json = new_employee, headers = my_headers)
        return resp.json() 
    