from address import Address
from address import Mailing

address_to = Address("Санкт-Петербург", "Лесная", "1", "13")
address_from = Address("Владивосток", "Морская", "13", "7")

mail = Mailing(address_to, address_from, "125", "Посылка")
mail.myTrack()
