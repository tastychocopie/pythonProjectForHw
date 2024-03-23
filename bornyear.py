true_born_year = 1799
end = 0
while end == 0:
    answer = int(input("В каком году родился А.С Пушкин?"))
    if answer == true_born_year:
        print("Верно")
        end += 1
    else:
        print("Неверно")