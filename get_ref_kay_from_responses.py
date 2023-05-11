import json
import csv

def getHeaders() -> list :
    return [
        'getscam_related_number'
        'founder_legal_entity'
        'purpose_product_loan'
        'court_general_jurisdiction'
        'biography'
        'сrimes'
        'banks'
    ]

count = 1

puss = './json_logs/'
csv_name = 'formated_data_getscam.csv'


while count < 49:
    key_list = []
    file_name = 'data_getscam_num'+str(count)+'.json'
    with open(puss + file_name, 'r' ) as f:
            data = f.read()
            json_data = json.loads(data)
            if json_data.get('data'):
                for element in json_data.get('data'):
                    if element not in key_list:
                        key_list.append(element)
                save(csv_name, json_data.get('data'),key_list)
    print('count=', count)
    count += 1

print('Done') 