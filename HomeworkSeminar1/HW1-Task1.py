# 1.Дано число, обозначающее день недели. Вывести его название и указать является ли он выходным
day_number = int(input("Введите число дня недели:   "))
def WeekEnd (number):
    if number > 0 and number <= 7:
        if number == 1:
            print(f"{number}й день недели - это понедельник, будний день.")
        if number == 2:
            print(f"{number}й день недели - это вторник, будний день.")
        if number == 3:
            print(f"{number}й день недели - это среда, будний день.")
        if number == 4:
            print(f"{number}й день недели - это четверг, будний день.")
        if number == 5:
            print(f"{number}й день недели - это пятница, будний день.")
        if number == 6:
            print(f"{number}й день недели - это суббота, выходной день.")
        if number == 7:
            print(f"{number}й день недели - это воскресенье, выходной день.")
    else:
        print("Неделя состоит из 7 дней. Введите число от 1 до 7, пожалуйста.")

WeekEnd (day_number)
