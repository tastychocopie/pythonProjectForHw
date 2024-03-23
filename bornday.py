true_born_year = 1799
bornday = "06.06"
loop_year = 0
while loop_year == 0:
    answer = int(input("В каком году родился А.С Пушкин?"))
    if answer == true_born_year:
        loop_year +=1
    else:
        print("Неверный год")

loop_day = 0
while loop_day == 0:
    day_answer = input("День рождения А.С Пушкина - ответ через точку ex. 05.09 [пятое сентября]")
    if day_answer == bornday:
        print("Верно")
        loop_day += 1
    else:
        print("Неверный день рождения")