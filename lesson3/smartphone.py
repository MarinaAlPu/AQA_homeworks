class Smartphone:
    def __init__(self, mark, model, number):
        self.mark = mark
        self.model = model
        self.number = number 
    def saySmartphone(self):
        print(self.mark + " - " + self.model + ".",int(self.number))     
