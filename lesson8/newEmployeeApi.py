import requests
import random

class Employee:
    def __init__(self, url):
        self.url = url

    def get_company_list(self):
        resp = requests.get(self.url + '/company')
        return resp.json()

    def get_random_employee_list(self):
        company_list = self.get_company_list()
        random_index = random.randint(0, len(company_list) - 1)
        random_company_id = company_list[random_index]['id']
        resp = requests.get(self.url + '/employee?company=' + str(random_company_id))        
        return resp.json()
    
    def get_specific_employee_list(self, id):
        resp = requests.get(self.url + '/employee?company=' + str(id))        
        return resp.json()
    
    def get_token(self, user = 'roxy', password = 'animal-fairy'):
        creds = { 
        'username' : user,
        'password' : password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]

    def add_new_company(self, name, description=''):
        new_company = {
            'name' : name,
            'description' : description
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
    