# Последняя цифра: (num % 101) // 100;
# Предпоследняя цифра: (num % 102) // 101;
# Предпредпоследняя цифра: (num % 103) // 102;
# .....
# Вторая цифра: (num % 10n-1) // 10n-2;
# Первая цифра: (num % 10n) // 10n-1.
# Нахождение циферок в 4-ехзначном числе
# a = int(input())
# a1 = (a % (10**4)) // (10**(4-1))
# a2 = (a % (10**(4-1))) // (10**(4-2))
# a3 = (a % (10**2)) // (10**1)
# a4 = (a % (10**1)) // (10**0)
# print(a1, a2, a3, a4)

'''
n = int(input())
while n != 0:            # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
                         # код обработки последней цифры
    n = n // 10          # удалить последнюю цифру из числа
'''
# Поиск чисел , удовлетворяющих определенным условиям в определенном диапазоне:
'''
for x in range(1, 33):
    for y in range(1, 33):
        for z in range(1, 33):
            for j in range(1, 33):
                if (x**3 + y**3 == z**3 + j**3) and x != y and x !=z and x != j and y != z and y != j and z != j:
                    print(x**3 + y**3)
                    
'''
# ПЕРЕВОД НАТУРАЛЬНЫХ ЧИСЕЛ В ДВОИЧНУЮ СИСТЕМУ
''' 
   a = int(input()) - ВВОДИМ ЧИСЛО
   counter = ''     - ВВОДИМ СЧЕТЧИК С НАЧАЛЬНЫМ ЗНАЧЕНИЕМ В ВИДЕ ПУСТОЙ СТРОКИ,
                      ТАК КАК 1 И 0 БУДЕМ СОБИРАТЬ В ЕДИНУЮ СТРОКУ ПОСТРОЧНО
   while a > 0:     - НАМ НАДО БУДЕТ НАЦЕЛО ДЕЛИТЬ НА 2 ПОКА ОСТАТКИ БУДУТ БОЛЬШЕ НУЛЯ
       counter += str(a % 2) - ЗАПИСЫВАЕМ ОСТАТКИ ОТ ДЕЛЕНИЯ НА 2 НАШЕГО ВВЕДЕННОГО ЧИСЛА,
                               ТАМ БУДУТ ЛИБО 1 ЛИБО 0 (ТК ЧИСЛА ЛИБО ЧЕТНЫЕ ЛИБО НЕЧЕТНЫЕ),
                               НАДО ИХ СОЕДИНИТЬ В ОДНУ СТРОКУ - ОТТОГО И ТАКАЯ ФОРМУЛА
                               
       a //= 2      - ПРОДОЛЖАЕМ ДЕЛИТЬ БЕЗ ОСТАТКА НА 2 ПОКА ИСХОДНОЕ ЧИСЛО НЕ СТАНЕТ НУЛЕМ
print(counter[::-1]) - ПЕРЕВОРАЧИВАЕМ СТРОКУ, ТАК КАК ИЗ ФОРМУЛ РАНЕЕ ЕДИНИЦЫ И НУЛИ ШЛИ ОТ КОНЦА К НАЧАЛУ

'''

# Дешифратор шифра цезаря по ASCII:
'''
cesar_step = int(input())                        - вводим шаг шифра
text = input()                                   - вводим зашифрованный текст
for symbol in text:                              - создаем цикл с новой переменной "symbols", которая будет
                                                   будет шагать посимвольно в зашифрованном тексте и принимать значения каждого символа этого текста
    text_new = ord(symbol) - cesar_step          - создаем переменную "text_new"; в нее мы будем закидывать значение кода АСКИ расшифрованного символа, а для этого
                                                   мы уменьшаем имеющийся код АСКИ у СИМВОЛА исходного текста на шаг шифра
                                                   
    if text_new < 97:                            - так как задача была на расшифровку текста с маленькими латинскими буквами, то нужно держаться диапазона значений
                                                   кода АСКИ от 97 по 122 включительно, там 26 значений (так как 97ой символ нам тоже нужен), поэтому, 
                                                   чтоб не сойти с диапазона и возвращаться в него надо создать данный цикл (если код станет меньше 97, то 
                                                   просто добавь к нему заветное 26 и вернешься в конец алфавита мелких латинских букв АСКИ, прямо правилам шифрования Цезаря)
                                                   и так с каждым символом зашифрованной строки
        text_new += 26
    print(chr(q_new), end='')                    - мы получили РАСШИФРОВАННЫЙ символ в виде кодировки АСКИ и нам нужно вывести теперь сам символ с помощью функции "chr()" и так
                                                   с каждым полученным символом. А чтоб все получилось в одну строчку, а не в каждой новой строке, юзаем параметр функции принта "end=''"
'''

# Вводим энное число чисел и составляем из них список, чтоб потом с этим списком работать
'''
n = int(input('Сколько чисел надо сложить? '))
counter = []
for i in range(n):
    x = [int(input())]
    counter += x
print(counter)
'''

# Умножаем буковки и выводим итог в форме списка
'''
a = ''
chara = 96
k = []
for j in range(1, 27):
    chara += 1
    a = [chr(chara) * j]
    k += a
print(k)

или

al = []
j = 1
for i in range(ord('a'), ord('z') + 1):
    al.append(chr(i) * j)
    j += 1
print(al)
'''

# Складываю соседние числа в списке и вывожу эти суммы в виде нового списка
'''
number_counter = int(input())
k = []
q = []
for i in range(number_counter):
    f = int(input())
    q.append(f)
    k.append(q[i] + q[i-1])
del k[0]
print(k)
'''

# Вставляю слова список так, чтоб удалялись одинаковые слова
'''
combos_need = int(input())
enemy = []
for i in range(combos_need):
    combo_on_hit = input()
    if combo_on_hit not in enemy:
        enemy.append(combo_on_hit)
print(*enemy, sep='\n')
'''

# Поиск одинаковых элементов в списке и подсчет количества этих совпадений
'''
text = input().split()
counter = 0

for i in range(len(text)):
    for j in range(i+1, len(text)):
        if text[i] == text[j]:
            counter += 1

print(counter)

'''
# Поиск СЛЕДУЮЩЕГО простого числа
'''
# объявление функции
def get_next_prime(num):
    n = num + 1
    while True:  # Есть граница, выше которой не надо
        # Запускаем перебор для проверки на делимость
        for i in range(2, n):  # От единицы до нашего числа включительно!
            if n % i == 0:  # Если нет остатка, то есть, число делится на что-то
                n += 1  # Добавляем единицу
                break  # Прерываем цикл
        else:  # Доперли до конца цикла
            return n  # Значит, наше число простое

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))

ИЛИ РЕКУРСИЕЙ:

# объявление функции
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num
    

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))
'''

# Проверка пароля на надежность
'''
def is_password_good(password):
    if len(password) < 8:
        return False
    flag1 = False
    flag2 = False
    flag3 = False
    for j in password:
        if j.isupper():
            flag1 = True
        if j.islower():
            flag2 = True
        if j.isdigit():
            flag3 = True
    return flag1 and flag2 and flag3
    
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))

ИЛИ

def is_password_good(password):
    upp = [i for i in password if i.isupper()] # создаем список из TRUE, если большие  буквы удут в пароле
    low = [i for i in password if i.islower()] # создаем список из TRUE, если маленькие буквы будут в пароле
    dig = [i for i in password if i.isdigit()] # создаем список из TRUE, если циферки будут в пароле
    return all([len(password) >= 8, upp, low, dig]) # получился список, состоящий из TRUE и/или FALSE 
                                                      (len(password) >= 8 - эта штука тоже выводит TRUE/FALSE 
                                                      в зависимости от результата сравнения), который в свою очередь 
                                                      обрабатывается функцией ALL, которая выдает TRUE, если список 
                                                      состоит из одних лишь TRUE и если хоть что-то будет в значении FALSE то
                                                      функция ALL выдаст FALSE


txt = input()                                  # вводим пароль
print(is_password_good(txt))                   # проверяем его с помощью созданной функции

'''

# Задачка на проверку Палиндрома
'''
# объявление функции
def is_pangram(text):
    glif = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    text = text.replace(' ', '')
    text = text.lower()
    for k in glif:
        if k not in text:
            return False
            
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))
'''

# Казино, которое всегда в выигрыше

"""
from random import randint
print('Угадай число, загаданное машиной, от 0 до 100!')
cpu_number = randint(1, 100)
x = True
while x == True:

    user_number = int(input('Какое число загадал компьютер? '))

    if user_number > cpu_number:
        print('Слишком много, попробуйте еще раз')
        x = True
    elif user_number < cpu_number:
        print('Слишком мало, попробуйте еще раз')
        x = True
    elif user_number == cpu_number:
        print('Вы угадали, поздравляем!')
        y = input('Попытаетесь угадать еще раз?').lower()
        if y == 'да':
            cpu_number = randint(1, 100)
            x = True
        else:
            print('До следующей встречи, пока ;-\)')
            x = False
"""

# Проект курса Пайтон для начинающих на Степик - Числовая угадайка
'''
from random import *
rand_number = randint(1, 100)
print('Добро пожаловать в числовую угадайку')
new_limit = 100
def is_valid(user_number, new_limit):
    if user_number.isdigit() and 1 <= int(user_number) <= new_limit:
        return True
    else:
        return False
counter = 0
flag = 0
while flag == 0:
    user_number = input('Введите число(в виде цифр):')
    x = is_valid(user_number, new_limit)
    if x == False:
        print(f'А может быть все-таки введем целое число от 1 до {new_limit}?')
        flag = 0
    else:
        work_number = int(user_number)
        if work_number < rand_number:
            print('Ваше число меньше загаданного, попробуйте еще разок')
            counter += 1
        elif work_number > rand_number:
            print('Ваше число больше загаданного, попробуйте еще разок')
            counter += 1
        elif work_number == rand_number:
            print('Вы угадали, поздравляем!')
            counter += 1
            print(f'Чудо произошло с {counter}-ой попытки')
            q = input('Желаете сыграть ещё раз?')
            if q == 'да':
                t = input('Желаете ли задать новое максимальное число для угадайки?')
                if t == 'да':
                    new_limit = int(input('Введите новую желаемую границу'))
                    rand_number = randint(1, new_limit)
                    counter = 0
                else:
                    rand_number = randint(1, 100)
                    counter = 0
                flag = 0
            else:
                break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
'''
