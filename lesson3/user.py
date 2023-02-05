#Создайте в классе 3 метода, которые печатают:
#    1. имя
#    2. фамилию
#    3. имя и фамилию

class User:
    def __init__(self, first_name, last_name):
        self.name1 = first_name
        self.name2 = last_name
    def sayName(self):
        print("Имя: ", self.name1)
    def sayFamily(self):
        print("Фамилия: ", self.name2)  
    def sayNameFamily(self):
        print("Имя, Фамилия: ", self.name1, self.name2)
