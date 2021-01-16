from random import randint

with open('text5.txt', 'w+', encoding='utf-8') as file:
    list_to_write = []
    for _ in range(0, 10):
        list_to_write.append(str(randint(0, 100)))
    file.write(' '.join(list_to_write))
    file.seek(0)
    print(sum(map(int, file.read().split(' '))))
