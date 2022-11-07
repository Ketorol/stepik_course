# Проверка на изограммность слова
'''
def is_isogram(string):
    string_list = [*string]
    string_list_upper = [*string.upper()]
    if len(string) == 0:
        return True
    for i in string_list:
        if string_list.count(i) > 1:
            return False
    for q in string_list_upper:
        if string_list_upper.count(q) > 1:
            return False
    return True
'''
# Возводим в квадрат циферки числа и из полученных чисел составляем новое ЧИСЛО
'''
def square_digits(num):
    digit_list = []
    x = 0
    if num == 0:
        return x
    while num != 0:
        last_digit = num % 10
        digit_list.append(str(last_digit**2))
        num = num // 10
    f = int((''.join(digit_list[::-1])))
    return f
'''
# Превращаю буквы в тексте в цифры согласно их позиции в алфавите.
'''
def alphabet_position(text):
    new_text_l = []
    alfabet = {'a': '1', 'b': '2', 'c': '3', 'd': '4', 'e': '5', 'f': '6', 'g': '7', 'h': '8', 
               'i': '9', 'j': '10', 'k': '11', 'l': '12', 'm': '13', 'n': '14', 'o': '15', 
               'p': '16', 'q': '17', 'r': '18', 's': '19', 't': '20', 'u': '21', 'v': '22', 
               'w': '23', 'x': '24', 'y': '25', 'z': '26'}
    for q in text.lower():
        for k in alfabet.keys():
            if q == k:
                new_text_l.append(alfabet.get(k))
            else:
                continue
    return ' '.join(new_text_l)
'''
