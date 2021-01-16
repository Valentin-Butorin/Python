import  re

result_dict = {}

with open('text_6.txt', encoding='utf-8') as file:
    list_of_strings = file.readlines()
    for string in list_of_strings:
        hours_str = re.findall(r"\w+", string)
        hours_int = list(map(int, filter(lambda x: x.isdigit(), hours_str)))
        result_dict[string.split(':')[0]] = sum(hours_int)
print(result_dict)
