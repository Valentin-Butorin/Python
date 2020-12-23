string = input()
string = string.split(' ')
for i, word in enumerate(string, 1):
    if len(word) > 10:
        print(i, word[:10])
    else:
        print(i, word[:10])
