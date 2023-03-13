import allure
class Users:
    def __init__(self, first_name: str, last_name: str, address: str, zip_code: str, city: str,\
                 country: str, email: str, phone_number: str, job_position: str, company: str):
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

    @allure.step("Получить имя пользователя")
    def my_first_name(self) -> str:
        return self.first_name

    @allure.step("Получить фамилию пользователя")    
    def my_last_name(self) -> str:
        return self.last_name

    @allure.step("Получить адрес пользователя")    
    def my_address(self) -> str:
        return self.address

    @allure.step("Получить zip-code пользователя")    
    def my_zip_code(self) -> str:
        return self.zip_code

    @allure.step("Получить город пользователя")    
    def my_city(self) -> str:
        return self.city

    @allure.step("Получить страну пользователя")    
    def my_country(self) -> str:
        return self.country

    @allure.step("Получить email пользователя")     
    def my_email(self) -> str:
        return self.email

    @allure.step("Получить телефон пользователя")    
    def my_phone_number(self) -> str:
        return self.phone_number   

    @allure.step("Получить должность пользователя")
    def my_job_position(self) -> str:
        return self.job_position

    @allure.step("Получить компанию пользователя")    
    def my_company(self) -> str:
        return self.company

user = Users("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "123@test.ru", "+79123456789", "QA", "SkyPro")