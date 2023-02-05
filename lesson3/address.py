class Address:
    def __init__(self, city, street, house, apartment):
        # self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.apartment = apartment
    def myAddress(self):
        return (self.city + ", " + self.street + ", " + self.house + " - " + self.apartment)

class Mailing:
    def __init__(self, address_to, address_from, cost, track):
        self.cost = cost
        self.track = track
        self.address_to = address_to
        self.address_from = address_from
    
    def myTrack(self):
        aT = self.address_to.myAddress()
        aF = self.address_from.myAddress()    
        print("Отправление", self.track, "из", aF, "в", aT, ". Стоимость", self.cost, "рублей")
