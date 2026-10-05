import random
fst = random.randint(1, 3)
f2st = random.randint(1, 3)
f3st = random.randint(1, 3)
f4st = random.randint(1, 5)
f5st = random.randint(1, 5)
f6st = random.randint(1, 5)
f7st = random.randint(1, 10)
f8st = random.randint(1, 10)
f9st = random.randint(1, 10)
fstscore = 0
nya = "Ну, гадай)"

print("Для начала введите свое имя")
name = str(input())
print('Привет!', name, ', ты попал в игру "Угадай-ка"')
print('Тебе нужны правила?')
print("1 - да, нужны \n2- нет, я все знаю")
knowly = int(input())
while True:
    if knowly == 1:
        print('Тут все очень просто.\n1. Компьютер загадывает число в тайне \n2. Ты должен отгадать это число')
        break
    elif knowly == 2:
        print('Отлично, перейдем к игре!')
        break
    else:
        print('Что? \nПросто напиши цифру 1 или 2')
        knowly = int(input())
print('Ну че, выбирай сложность \n1. Лёгкий \n2. Средний \n3. Босс')
lvl = int(input())
if lvl == 1:
    print(nya)
    flvlfrnd = int(input())
    if flvlfrnd == fst:
        print('Правильно!')
        fstscore+=1
    else:
        print('Нет')
    f2lvlfrnd = int(input())
    if f2lvlfrnd == f2st:
        print('Правильно!')
        fstscore+=1
    else:
        print('Нет')
    f3lvlfrnd = int(input())
    if f3lvlfrnd == f3st:
        print('Правильно!')
        fstscore+=1
    else:
        print('Нет')
    print("Готово, твой счет", fstscore,"/ 3")
if lvl == 2:
    print(nya)
    f4lvlfrnd = int(input())
    if f4lvlfrnd == f4st:
        print('Правильно!')
        fstscore+=3
    else:
        print('Нет')
    f5lvlfrnd = int(input())
    if f5lvlfrnd == f5st:
        print('Правильно!')
        fstscore+=3
    else:
        print('Нет')
    f6lvlfrnd = int(input())
    if f6lvlfrnd == f6st:
        print('Правильно!')
        fstscore+=3
    else:
        print('Нет')
    print("Готово, твой счет", fstscore,"/ 9")
if lvl == 3:
    print(nya)
    f7lvlfrnd = int(input())
    if f7lvlfrnd == f7st:
        print('Правильно!')
        fstscore+=10
    else:
        print('Нет')
    f8lvlfrnd = int(input())
    if f8lvlfrnd == f8st:
        print('Правильно!')
        fstscore+=10
    else:
        print('Нет')
    f9lvlfrnd = int(input())
    if f9lvlfrnd == f9st:
        print('Правильно!')
        fstscore+=10
    else:
        print('Нет')
    print("Готово, твой счет", fstscore,"/ 30")
