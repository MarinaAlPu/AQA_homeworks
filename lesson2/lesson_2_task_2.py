# year = input("Год: ")
# year = int(year)

# def is_year_leap(year):
#     if (year % 4 == 0):
#         x = True
#     else:
#         x = False
#     return x

# result = is_year_leap(year)    
# print("год ", year, ":", result)

# меньше строк
def is_year_leap(year):
    if (year % 4 == 0):
        x = True
    else:
        x = False
    return x
    
year = input("Год: ")  
print("Год ", year, ":", is_year_leap(int(year)))

# С ПРОВЕРКОЙ НА ОТРИЦАТЕЛЬНОСТЬ
# year = input("Год: ")
# year = int(year)

# def is_year_leap(year):
#     import math
#     for year in range(int(-math.inf), 0): # КАК ОБОЗНАЧИТЬ ДИАПАЗОН ОТ -БЕСКОНЕЧНОСТИ ДО 0
#         print("Введите положительное значение: ")
#         year = input("Год: ")
#         year = int(year) 
#     
#         if (year % 4 == 0):
#             x = True
#         else:
#             x = False
#         return x

# result = is_year_leap(year)    
# print("год ", year, ":", result)    