from defs import set_grade, SolvedResoult, file_log
from random import randint, choice

shots = 0
right_num =0
errors_num = 0
user_result = ''
difficult = 1

print("Для выхода введите q.\n")

difficult = int(input('Введите уровень сложности: '))

while True:
    if user_result == 'q':
        break
    number_1 = randint(1,10**difficult)
    number_2 = randint(1,10**difficult)
    request = '{} {} {}'.format(number_1, choice('+-*'), number_2)
    question = "Сколько будет {}?".format(request)
    print(question)
    right_result = eval(request)
    user_result = input()
    if user_result != 'q':
        if int(user_result.isnumeric()):
            shots += 1
            file_log(question,right_result,user_result)
            if SolvedResoult(right_result,int(user_result)):
                right_num += 1
            else:
                errors_num += 1
        else:
            continue
    else:
        break

if shots > 0:
    grade = set_grade(shots, errors_num)
    print("\nВсего ответов: {}\nПравильных ответов: {}\
           \nНеправильных ответов: {}\nОценка: {}".format(
           shots, right_num, errors_num, grade))

