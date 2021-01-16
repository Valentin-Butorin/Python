with open('text1.txt', 'a+', encoding='utf-8') as file:
    line = input()
    while line:
        file.write(f'{line}\n')
        line = input()
    file.seek(0)
    print(file.read())
