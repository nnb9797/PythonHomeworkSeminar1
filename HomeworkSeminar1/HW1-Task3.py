#3) Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка.
# *Пример:*
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
coordinate_number_x = float(input("Введите координату X, число не равное (0):  "))
coordinate_number_y = float(input("Введите координату Y, число не равное (0):  "))

def CoordinateSystem (x, y):
    if x == 0 or y == 0:
        print("Вы ввели нулевое значение!")
    else:
        if x > 0 and y > 0:
                print("Точка находится в 1й четверти")
        elif x < 0 and y > 0:
                print("Точка находится во 2й четверти")
        elif x < 0 and y < 0:
                print("Точка находится в 3й четверти")
        elif x > 0 and y < 0:
                print("Точка находится в 4й четверти")
    return x, y

CoordinateSystem (coordinate_number_x, coordinate_number_y)