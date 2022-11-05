# Проект - Числовая угадайка
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
# Проект - Магический шар 8
'''
from random import *
answers = ['Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом', 'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да', 'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять', 'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно']
print('Привет. Я, магический шар. Я знаю ответ на любой твой вопрос.')
user_name = input('Как тебя зовут, дружище? ')
print(f'Привет, {user_name}!')
flag = 0
while flag == 0:
    question = input('Задавай свой вопрос? ')
    print(choice(answers))
    request = input('Ещё вопросы есть? (выбирай: "да" или "нет") ')
    if request == 'да':
        flag = 0
    else:
        print('Возвращайся если возникнут вопросы!')
        flag = 1
'''

# генератор паролей
'''
from random import *
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars_inpass = ''
pass_counts = int(input('Сколько паролей Вам надо придумать? '))
pass_len = int(input('Какой длины должен быть пароль? '))
numbers_inpass = input('Добавить в пароль цифры? ("да" или "нет") ')
upperletter_inpass = input('Добавить в пароль большие буквы? ("да" или "нет") ')
lowerletter_inpass = input('Добавить ли в пароль маленькие буквы? ("да" или "нет") ')
punct_inpass = input('Добавить ли в пароль символы? ("да" или "нет") ')
same_symbols = input('Исключать ли в пароле символы - "il1Lo0O"? ("да" или "нет") ')

def yes_no(word):
    x = True
    if word == 'да':
        return True
    else:
        return False
    return x

if yes_no(numbers_inpass) == True:
    chars_inpass += digits
if yes_no(upperletter_inpass) == True:
    chars_inpass += uppercase_letters
if yes_no(lowerletter_inpass) == True:
    chars_inpass += lowercase_letters
if yes_no(punct_inpass) == True:
    chars_inpass += punctuation
if yes_no(same_symbols) == True:
    for q in 'il1Lo0O':
        if q in chars_inpass:
            chars_inpass = chars_inpass.replace(q, '')

def generate_password(pass_counts, pass_len):
    gen_pass = ''
    for i in range(pass_counts):
        gen_pass += " "
        for q in range(pass_len):
            gen_pass += choice(chars_inpass)
    return gen_pass.split()

pass_gened = generate_password(pass_counts, pass_len)
print(*pass_gened, sep='\n')
'''

