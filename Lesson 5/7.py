import json

result =[{}, {}]
with open('text_7.txt', encoding='utf-8') as file:
    lines = file.readlines()
    for string in lines:
        string = string.replace('\n', '')
        profit = int(string.split(' ')[-2]) - int(string.split(' ')[-1])
        result[0][string.split(' ')[0]] = profit
    positive_profit = list(filter(lambda x: x > 0, result[0].values()))
    average = sum(positive_profit) / len(positive_profit)
    result[1]['average_profit'] = average

print(result)

with open('output.json', 'w', encoding='utf-8') as output_file:
    json.dump(result, output_file)
