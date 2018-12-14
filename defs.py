def set_grade(shots, errors_num):
    errors_prop = errors_num / shots
    if errors_prop < 0.1:
        grade = '5 -'
    elif errors_prop < 0.3:
        grade = '4'
    elif errors_prop <= 0.5:
        grade = '3'
    else:
        grade = '2'
    return grade

def file_log(Question,Right_Resoult,User_Resoult):
    with open("UserTryLog.txt","a+") as fs:
         fs.write("Вопрос: {}\nПравильный ответ: {}\nОтвет пользователя: {}\n\n".format(
                    Question,Right_Resoult,User_Resoult))



def SolvedResoult(Right_Resoult,User_Resoult):
    if User_Resoult == Right_Resoult:
        print("Правильно!\n")
        return True
    else:
        print("Не правильно!\nПравильный ответ: {}\n".format(
            str(Right_Resoult)))
        return False

