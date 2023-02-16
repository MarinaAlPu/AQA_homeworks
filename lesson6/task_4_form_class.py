class Users:
    def __init__(self, first_name, last_name, address, zip_code, city, country, email, phone_number, job_position, company):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.zip_code = zip_code
        self.city = city
        self.country = country
        self.email = email
        self.phone_number = phone_number
        self.job_position = job_position
        self.company = company

    def my_first_name(self):
        return self.first_name
    
    def my_last_name(self):
        return self.last_name
    
    def my_address(self):
        return self.address
    
    def my_zip_code(self):
        return self.zip_code
    
    def my_city(self):
        return self.city
    
    def my_country(self):
        return self.country
     
    def my_email(self):
        return self.email
    
    def my_phone_number(self):
        return self.phone_number   

    def my_job_position(self):
        return self.job_position
    
    def my_company(self):
        return self.company

user = Users("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "123@test.ru", "+79123456789", "QA", "SkyPro")