# 4. 4) Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек
# в этой четверти (x и y).
q = int(input("Задайте координатную четверть, число не равное 0, в диапазоне от 1 до 4:  "))

def CoordinateQuarter (q):
    if q == 0 or q < 1 or q > 4:
        print ("Вы ввели неверное значение!")
    else:
        if q == 1:
                print("Допустимые значения координат: x > 0, y > 0")
        elif q == 2:
                print("Допустимые значения координат: x < 0, y > 0")
        elif q == 3:
                print("Допустимые значения координат: x < 0, y < 0")
        elif q == 4:
                print("Допустимые значения координат: x > 0, y < 0")
    return q

CoordinateQuarter (q)