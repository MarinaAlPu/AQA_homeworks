# Написать функцию month_to_season(),
# которая принимает 1 аргумент - номер месяца -
# и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем 'Зима'.

# def month_to_season(m):
#     if (m == 12) or (m == 1) or (m == 2):
#         print("Winter")
#     elif (m == 3) or (m == 4) or (m == 5):
#         print("Spring")
#     elif (m == 6) or (m == 7) or (m == 8):
#         print("Summer")
#     else:
#         print("Autumn")

# month_to_season(1)

# код меньше
def month_to_season(m):
    if 3 <= m <= 5:
        print("Spring")
    elif 6 <= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Autumn")
    else:
        print("Winter")

month_to_season(int(input("Номер месяца: ")))