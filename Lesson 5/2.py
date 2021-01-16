with open('text2.txt', encoding='utf-8') as file:
    all_lines = file.readlines()
    print(f'Количество строк - {len(all_lines)}')
    for i, line in enumerate(all_lines, 1):
        line = line.replace('\n', '')
        print(f'Количество слов в {i} строке - {len(line.split(" "))}.')
