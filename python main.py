import random
import time
fst = random.randint(1, 3)
f2st = random.randint(1, 3)
f3st = random.randint(1, 3)
f4st = random.randint(1, 5)
f5st = random.randint(1, 5)             #random numbers generation
f6st = random.randint(1, 5)
f7st = random.randint(1, 10)
f8st = random.randint(1, 10)
f9st = random.randint(1, 10)
fstscore = 0
nya = "Выбирай"

print("Для начала введите свое имя")
name = str(input())
print('Привет!', name, ', ты попал в игру "Угадай-ка"')
print('Тебе нужны правила?')
time.sleep(0.6)
print("1 - да, нужны \n2- нет, я все знаю")
knowly = int(input())
while True:
    if knowly == 1:      #check, players wants to read rules or no
        time.sleep(0.5)
        print('Тут все очень просто. \n1. Компьютер загадывает число в тайне \n2. Ты должен отгадать это число')
        break
    elif knowly == 2:
        time.sleep(0.5)
        print('Отлично, перейдем к игре!')
        break
    else:
        time.sleep(0.5)
        print('Что? \nПросто напиши цифру 1 или 2')     #if player write unknow char
        knowly = int(input())
print('Выбирай сложность \n1. Изи \n2. Средний \n3. Босс')   #level select
lvl = int(input())
if lvl == 1:
    print(nya)
    flvlfrnd = int(input())
    if flvlfrnd == fst:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=1
    else:
        time.sleep(0.5)
        print('Нет')
    f2lvlfrnd = int(input())
    if f2lvlfrnd == f2st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=1
    else:
        time.sleep(0.5)
        print('Нет')
    f3lvlfrnd = int(input())
    if f3lvlfrnd == f3st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=1
    else:
        time.sleep(0.5)
        print('Нет')
    time.sleep(0.5)
    print("Готово, твой счет", fstscore,"/ 3")    #shows score
if lvl == 2:
    print(nya)
    f4lvlfrnd = int(input())
    if f4lvlfrnd == f4st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=3
    else:
        time.sleep(0.5)
        print('Нет')
    f5lvlfrnd = int(input())
    if f5lvlfrnd == f5st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=3
    else:
        print('Нет')
        time.sleep(0.5)
    f6lvlfrnd = int(input())
    if f6lvlfrnd == f6st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=3
    else:
        time.sleep(0.5)
        print('Нет')
    time.sleep(0.5)
    print("Готово, твой счет", fstscore,"/ 9")
if lvl == 3:
    print(nya)
    f7lvlfrnd = int(input())
    if f7lvlfrnd == f7st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=10
    else:
        time.sleep(0.5)
        print('Нет')
    f8lvlfrnd = int(input())
    if f8lvlfrnd == f8st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=10
    else:
        time.sleep(0.5)
        print('Нет')
    f9lvlfrnd = int(input())
    if f9lvlfrnd == f9st:
        time.sleep(0.5)
        print('Правильно!')
        fstscore+=10
    else:
        time.sleep(0.5)
        print('Нет')
    time.sleep(0.5)
    print("Готово, твой счет", fstscore,"/ 30")
