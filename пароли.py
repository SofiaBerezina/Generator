print('Введите пароль')
password = input()
length=0
numbers=0
capitallet=0
special='|<>?!@#$%^&*()_+=-~`'
small = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбюё'
big = 'QWERTYUIOPASDFGHJKLZXCVBNMЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ'
spec=0
for i in password:
    if small.count(i)>=1:
        capitallet+=0.5
    if big.count(i)>=1:
        capitallet+=0.5
for i in special:
    if password.count(i)>=1:
        spec+=1
if len(password)>=12:
    length+=1
elif len(password)>=8 and len(password)<12:
    length+=0.5
if password.isalpha()==False:
    numbers+=0.5
if password.isdigit()==False:
    numbers+=0.5
if length==0 and (numbers==0 or numbers==0.5) and (capitallet==2 or capitallet==0 or capitallet==1) :
    print('Пароль ненадежный')
elif (length==0 or length==0.5) and (numbers==0 or numbers==1 or numbers==0.5) and (capitallet==0 or capitallet==2 or capitallet==1):
    print('Легкий пароль')
elif (length==0.5 and numbers==1 and (capitallet==1 or capitallet==2)) or (length==1 and (numbers==1 and capitallet==1)):
    print('Средний пароль')
elif length==1 and numbers==1 and capitallet==2 and spec>=1:
    print('Сложный пароль')
