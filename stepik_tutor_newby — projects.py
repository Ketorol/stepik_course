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

# Шифратор Цезаря (каждое слово шифруется на сдвиг, равный длине этого слова)
'''
orig_text = input()
orig_text_copy = orig_text
for q in orig_text_copy:
    if q in '*,.!@"-':
        orig_text_copy = orig_text_copy.replace(q, '')
orig_text_copy_list = [len(i) for i in orig_text_copy.split()]
count = 0
word = ''

for f in orig_text:
    number = ord(f)
    if f == ' ':
        count += 1
        word += f
    elif 65 <= number <= 90:
        if number + orig_text_copy_list[count] > 90:
            word += chr(number + orig_text_copy_list[count] - 26)
        else:
            word += chr(number + orig_text_copy_list[count])
    elif 97 <= number <= 122:
        if number + orig_text_copy_list[count] > 122:
            word += chr(number + orig_text_copy_list[count] - 26)
        else:
            word += chr(number + orig_text_copy_list[count])
    else:
        word += f
print(word)
'''
# Переводчик из 10-ой системы в любую другую указанную юзером
'''
num = int(input())
base = int(input())

def trans_10_to_base(num, base=2):
    res = ''
    while num:
        num, d = divmod(num, base)
        sd = str(d) if d < 10 else chr(ord('A') + d - 10)
        res = sd + res
    return res
print(trans_10_to_base(num, base))
'''

# Игра - виселица
'''
from random import *
word_list = ['файтинг', 'фаталити', 'бросок', 'подножка', 'шорьюкен', 'скорпион', 'рю', 'саб-зиро', 'кен', 'казуя', 'кинг', 'мортуха', 'эсэф', 'теккен']

def get_word():
    word = choice(word_list).upper()
    return word

def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    ''',
        # голова, торс, обе руки, одна нога
        '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / 
                       -
                    ''',
        # голова, торс, обе руки
        '''
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |      
                       -
                    ''',
        # голова, торс и одна рука
        '''
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |     
                       -
                    ''',
        # голова и торс
        '''
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |     
                       -
                    ''',
        # голова
        '''
                       --------
                       |      |
                       |      O
                       |    
                       |      
                       |     
                       -
                    ''',
        # начальное состояние
        '''
                       --------
                       |      |
                       |      
                       |    
                       |      
                       |     
                       -
                    '''
    ]
    return stages[tries]

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Давайте играть в угадайку слов!')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input('Введите букву или слово целиком: ').upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print('Вы уже называли букву', guess)
            elif guess not in word:
                print('Буквы', guess, 'нет в слове.')
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Отличная работа, буква', guess, 'присутствует в слове!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('Вы уже называли слово', guess)
            elif guess != word:
                print('Слово', guess, 'не является верным.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Поздравляем, вы угадали слово! Вы победили!')
    else:
        print('Вы не угадали слово. Загаданным словом было ' + word + '. Может быть в следующий раз!')
again = 'д'

while again.lower() == 'д':
    word = get_word()
    play(word)
    again = input('Играем еще раз? (д = да, н = нет):')
'''