
import re


def password_level(password):
    symbols = '!@#$%^&*(){}[]|\/~`_-+=?.,;%№:'
    protection = 0
    if len(password) < 6:
        print('Недопустимый пароль')
    else:
        if re.search('[0-9]', password):
            protection += 1
        if re.search('[a-z]', password) or re.search('[а-я]', password):
            protection += 1
        if re.search('[A-Z]', password) or re.search('[А-Я]', password):
            protection += 1
        for i in password:
            if i in password:
                protection += 1
                break
    if protection == 1:
        print('Допустимый пароль')
    elif protection == 2:
        print('Легкий пароль')
    elif protection == 3:
        print('Средний пароль')
    elif protection == 4:
        print('Сложный пароль')


password_level('123!4567rfg@DDDds')
