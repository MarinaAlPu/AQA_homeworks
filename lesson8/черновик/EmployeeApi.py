import requests
import random

class Employee:
    def __init__(self, url):
        self.url = url

    def get_company_list(self):
# - Получить любую организацию из списка
        resp = requests.get(self.url + '/company')
        return resp.json()
    
# количество компаний в списке
    def get_quantity_in_company_list(self):
        resp = requests.get(self.url + '/company')
        company_body = resp.json()       
        quantity = len(company_body)
#        print("Количество компаний в первоначальном списке: " + str(quantity))
        return resp.json() 
    
# произвольный индекс
    def get_random_index(self):
        resp = requests.get(self.url + '/company')
        company_body = resp.json()        
        quantity = len(company_body)        
        random_index = random.randint(0, quantity - 1)
#        print("Произвольный индекс компании: " + str(random_index))
        return resp.json() 

# id по произвольному индексу
    def get_random_id(self):
        resp = requests.get(self.url + '/company')
        company_body = resp.json()
        quantity = len(company_body)        
        random_index = random.randint(0, quantity - 1)
        random_id = company_body[random_index]["id"]
#        print("id копмании, найденной по произвольному индексу: " + str(random_id))
        return resp.json() 
#        my_name = company_body[random_index]["name"]
#        print("название копмании, найденной по произвольному индексу: " + str(my_name))

# - Получить список сотрудников произвольной компании
    def get_random_employee_list(self, params_to_add = None):
        resp1 = requests.get(self.url + '/company', params = params_to_add)
        company_body = resp1.json() 
        quantity = len(company_body)          
        random_index = random.randint(0, quantity - 1)
        random_id = company_body[random_index]["id"]
#        print("id копмании, найденной по произвольному индексу: " + str(random_id))
#        my_name = company_body[random_index]["name"]
#        print("название копмании, найденной по произвольному индексу: " + str(my_name))
        resp = requests.get(self.url + '/employee?company=' + str(random_id))
        employee_body = resp.json()

        if len(employee_body) == 0:
            print("В компании нет сотрудников.")
        else:
            print("В компании числится " + str(len(employee_body)) + " сотрудников.")

        return resp.json() 

# - Получить токен
    def get_token(self, user = 'roxy', password = 'animal-fairy'):
        creds = { 
        'username' : user,
        'password' : password
        }
        resp = requests.post(self.url + '/auth/login', json=creds)
        return resp.json()["userToken"]  

# - Cоздать новую компанию
    def add_new_company(self, name, description = ''):
        new_company = { 
            'name': name,
            'description': description
        }
        
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        resp = requests.post(self.url + '/company', json=new_company, headers = my_headers)
        return resp.json()        

# - Получить список сотрудников
    def get_employee_list(self, id):
        resp = requests.get(self.url + '/employee?company=' + str(id))
        return resp.json()
        employee_body_before = resp.json()


# - Получить количество сотрудников
    def get_employee_quantity(self, id):
        resp = requests.get(self.url + '/employee?company=' + str(id))

        employee_body_before = resp.json()
        return employee_body_before        
        staff_before = len(employee_body_before)

# добавить сотрудника
    def add_new_employee(self, id, first_name, last_name, middle_name, phone, url):
        new_employee = {
            'companyId': id,
            'firstName': first_name,
            'lastName': last_name,
            'middleName': middle_name,
            'phone': phone,
            'url': url
    }

        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        resp = requests.post(self.url + '/employee', json=new_employee, headers = my_headers)
        return resp.json()

# - Удалить компанию
    def delete_company(self, id):
        id = 513
        my_headers = {}
        my_headers['x-client-token'] = self.get_token()

        x = self.url + '/company/delete/' + str(id)
        print(x)
        resp = requests.get(self.url + '/company/delete/' + str(id), headers = my_headers)
        return  resp.json()

# - Получить информацию по любому id сотрудника (получаю по id добавленного сотрудника)
    def get_employee_info(self, id):
        resp = requests.get(self.url + '/employee/' + str(id))
        return  resp.json()

url = "https://x-clients-be.onrender.com"
id = 513
x = url + '/company/delete/' + str(id)
print(x)

