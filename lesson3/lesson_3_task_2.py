from smartphone import Smartphone

smartphone1 = Smartphone("Samsung", "Galaxy s10e", "+79111111111")
smartphone2 = Smartphone("SonyEricsson", "K750i", "+79222222222")
smartphone3 = Smartphone("Nokia", "G400", "+79333333333")
smartphone4 = Smartphone("iPhone", "14 Pro Max", "+79444444444")
smartphone5 = Smartphone("Xiaomi", "Redmi 5", "+79555555555")

catalog = [smartphone1,smartphone2,smartphone3,smartphone4,smartphone5]

for smartphone in catalog:
    smartphone.saySmartphone()