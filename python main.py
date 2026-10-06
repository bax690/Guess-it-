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
nya = "Выбирай!"
nya_en = "Guess!"
right_or_no = ('Правильно', 'Нет')
right_or_no_en = ('Right', 'No')

print("[RU]Давайте выберем язык \n[EN]Let's choose a language.")
print('1 - Русский \n2 - English')
language = int(input())
if language == 1:
    print("Введите свое имя")
else:
    print('Enter your name')
name = str(input())
if language == 1:
    print('Привет!', name, ', ты попал в игру "Угадай-ка"')
    print('Тебе нужны правила?')
else:
    print('Hello!', name, 'you are in the game "Guess it!"')
    print('You need rules?')
time.sleep(0.6)
if language == 1:
    print("1 - да, нужны \n2- нет, я все знаю")
else:
    print("1 - Yes, I need rules \n2 - No problem")
knowly = int(input())
while True:
    if knowly == 1:      #check, players wants to read rules or no
        time.sleep(0.5)
        if language == 1:
            print('Тут все очень просто. \n1. Компьютер загадывает число в тайне \n2. Ты должен отгадать это число')
        else:
            print("It's very simple. \n1. The computer think about a random number \n2. You have to guess this number")
        time.sleep(3.5)
        break
    elif knowly == 2:
        time.sleep(0.5)
        if language == 1:
            print('Отлично, перейдем к игре!')
        else:
            print("Great, let's move on to the game!")
        break
    else:
        time.sleep(0.5)
        if language == 1:
            print('Что? \nПросто напиши цифру 1 или 2')
        else:
            print('What? \nJust write the numbers 1 or 2')
                 #if player write unknow char
        knowly = int(input())
if language == 1:
    print('Выбирай сложность \n1. Изи \n2. Средний \n3. Босс')
else:
    print('Choose a lvl \n1. Easy \n2. Middle \n3. Boss')   #level select
lvl = int(input())
if lvl == 1:
    if language == 1:
        print(nya)
    else:
        print(nya_en)
    flvlfrnd = int(input())
    if flvlfrnd == fst:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=1
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    f2lvlfrnd = int(input())
    if f2lvlfrnd == f2st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=1
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1]) 
    f3lvlfrnd = int(input())
    if f3lvlfrnd == f3st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=1
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    time.sleep(0.5)
    if language == 1:
        print("Готово, твой счет", fstscore,"/ 3")
    else:
        print("Done, your score is", fstscore,"/ 3")
    time.sleep(1010101010101010)#shows score
if lvl == 2:
    if language == 1:
        print(nya)
    else:
        print(nya_en)
    f4lvlfrnd = int(input())
    if f4lvlfrnd == f4st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=3
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    f5lvlfrnd = int(input())
    if f5lvlfrnd == f5st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=3
    else:
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
        time.sleep(0.5)
    f6lvlfrnd = int(input())
    if f6lvlfrnd == f6st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=3
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    time.sleep(0.5)
    if language == 1:
        print("Готово, твой счет", fstscore,"/ 9")
    else:
        print("Done, your score is", fstscore,"/ 9")
    time.sleep(1010101010101010)
if lvl == 3:
    if language == 1:
        print(nya)
    else:
        print(nya_en)
    f7lvlfrnd = int(input())
    if f7lvlfrnd == f7st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=10
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    f8lvlfrnd = int(input())
    if f8lvlfrnd == f8st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=10
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    f9lvlfrnd = int(input())
    if f9lvlfrnd == f9st:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[0])
        else:
            print(right_or_no_en[0])
        fstscore+=10
    else:
        time.sleep(0.5)
        if language == 1:
            print(right_or_no[1])
        else:
            print(right_or_no_en[1])
    time.sleep(0.5)
    if language == 1:
        print("Готово, твой счет", fstscore,"/ 30")
    else:
        print("Done, your score is", fstscore,"/ 30")
    time.sleep(1010101010101010)
