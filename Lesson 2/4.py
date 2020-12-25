string = input()
string = string.split(' ')
for i, word in enumerate(string, 1):
    print(i, word[:10])
