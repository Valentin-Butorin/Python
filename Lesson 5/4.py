translate_dict = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

with open('input4.txt', encoding='utf-8') as input_file:
    with open('output4.txt', 'w', encoding='utf-8') as output_file:
        number_of_strings = len(input_file.readlines())
        input_file.seek(0)
        for i, string in enumerate(input_file.readlines(), 0):
            if i == 0:
                input_file.seek(0)
            to_replace = input_file.readline().split(' - ')[0]
            output_file.write(string.replace(to_replace, translate_dict[to_replace]))
