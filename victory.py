# Choose 5 people
# 1 Lionel Messi 1987
# 2 Elon Musk 1971
# 3 Steve Jobs 1955
# 4 Christiano Ronaldo 1985
# 5 Jeon Jungkook 1997
messi_born_year = 1987
elon_born_year = 1971
steve_born_year = 1955
ronaldo_born_year = 1985
jk_born_year = 1997
play_again = "да"
while play_again == "да":
    correct_counter = 0
    incorrect_counter = 0
    print("Привет! Добропожаловать на викторину! Ответы принимаются ввиде цифр(чисел) ")
    answer_messi = int(input("Вопрос 1. В каком году родился Лионель Мэсси?"))
    if answer_messi == messi_born_year:
        correct_counter += 1
    else:
        incorrect_counter += 1
    answer_elon = int(input("Вопрос 2. В каком году родился Илон Маск?"))
    if answer_elon == elon_born_year:
        correct_counter += 1
    else:
        incorrect_counter += 1
    answer_steve = int(input("Вопрос 3. В каком году родился Стив Джобс?"))
    if answer_steve == steve_born_year:
        correct_counter += 1
    else:
        incorrect_counter += 1
    answer_ronaldo = int(input("Вопрос 4. В каком году родился Криштиану Роналду?"))
    if answer_ronaldo == ronaldo_born_year:
        correct_counter += 1
    else:
        incorrect_counter += 1
    answer_jk = int(input("Вопрос 5. В каком году родился Чонгук?"))
    if answer_jk == jk_born_year:
        correct_counter += 1
    else:
        incorrect_counter += 1
    print("РЕЗУЛЬТАТ:")
    print("Количество правильных ответов: ", correct_counter)
    print("Количество ошибок: ", incorrect_counter)
    correct_percent = correct_counter * 100 / 5
    print("Процент правильных ответов: ", correct_percent, "%")
    incorrect_percent = incorrect_counter * 100 / 5
    print("Процент ошибок", incorrect_percent, "%")
    play_again = input("Хочешь заново сыграть?")
    if play_again == "да":
        play_again = "да"
    else:
        play_again = "нет"