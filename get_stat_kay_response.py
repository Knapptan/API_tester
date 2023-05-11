import json

filed_name = 'headers_stat.json'
key_stat = []

with open("otus.txt", "r") as file:
                for i in file:
                    ii = i.replace('\n', '')
                    res_str= ii.replace(' ', '')
                    if i not in key_stat:
                        key_stat.append(res_str)
                    # if i not in key_stat:
# print(key_stat)

seted_keylist = set(key_stat)
seted_key_no_num = []
for elemint in seted_keylist:
    if elemint.isdigit() == False:
           seted_key_no_num.append(elemint)
           
key_stat_no_num = []

for elemint in key_stat:
    if elemint.isdigit() == False:
           key_stat_no_num.append(elemint)

# print(key_stat_no_num)

# print(key_stat)
# print(seted_key_no_num)
dict_response = dict.fromkeys(seted_key_no_num, 0)
# print(dict_response)
for element in key_stat:
       if element in key_stat_no_num:
            # print(element)
            dict_response[element]+= 1

print(dict_response)

with open(filed_name, '+w') as file:
    json.dump(dict_response, file,ensure_ascii=False, indent=4)