class Users:
    def __init__(self, firstName, lastName, address, zipCode, city, country, email, phoneNumber, jobPosition, company):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.zipCode = zipCode
        self.city = city
        self.country = country
        self.email = email
        self.phoneNumber = phoneNumber
        self.jobPosition = jobPosition
        self.company = company

    def myFirstName(self):
        return self.firstName
    
    def myLastName(self):
        return self.lastName
    
    def myAddress(self):
        return self.address
    
    def myZipCode(self):
        return self.zipCode
    
    def myCity(self):
        return self.city
    
    def myCountry(self):
        return self.country
     
    def myEmail(self):
        return self.email
    
    def myPhoneNumber(self):
        return self.phoneNumber    

    def myJobPosition(self):
        return self.jobPosition
    
    def myCompany(self):
        return self.company
    
    # def test_background_color_green(locator):
    # x = driver.find_element(By.CSS_SELECTOR, locator)
    # y = x.value_of_css_property("background-color")
    # print(y)
    

user = Users("Иван", "Петров", "Ленина, 55-3", "", "Москва", "Россия", "123@test.ru", "+79123456789", "QA", "SkyPro")

# user.myFirstName()
# user.myLastName()
# user.myAddress()
# user.myZipCode()
# user.myCity()
# user.myCountry()
# user.myEmail()
# user.myPhoneNumber()
# user.myJobPosition()
# user.myCompany()

# print(user.myFirstName() + " " + 
# user.myLastName() + ", " +  
# user.myAddress() + ", " +  
# user.myZipCode() + ", " +  
# user.myCity() + ", " +  
# user.myCountry() + ", " +  
# user.myEmail() + ", " +
# user.myPhoneNumber() + ", " +
# user.myJobPosition() + " " +  
# user.myCompany())

# fn = str(user.myFirstName())
# print(fn)