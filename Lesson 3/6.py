def int_func(word):
    new_word = ''
    for char in word:
        new_word += chr(ord(char) - 32)
        break
    for i in range(1, len(word)):
        new_word += word[i]
    return new_word


def title_words_in_string(string):
    string_list = check_input(string).split(' ')
    new_list = []
    for elem in string_list:
        new_list.append(int_func(elem))
    new_string = ' '.join(new_list)
    return new_string


def check_input(string):
    string_list = string.split(' ')
    for elem in string_list:
        for char in elem:
            if ord(char) < 97 or ord(char) > 122:
                return check_input(str(input(
                    f'Слово "{elem}" содержит запрещенный символ - "{char}".\n'
                    f'Повторите ввод, используя только латинские '
                    f'буквы нижнего регистра: ')))
    return string


text = str(input('Введите слова разделенные пробелом: '))
print(title_words_in_string(text))
