import json
import csv

def getHeaders() -> list :
    return ["getscam_age", "getscam_place_bith", "acquaintance_1", "getscam_related_number", "emails", "whatsapps", "boss_phone", "getscam_addresses", "children", "getscam_phone_book", "vks", "fbs", "oks", "instagrams", "first_activities_internet_getscam", "getscam_work_place", "getscam_summ_income", "getscam_profession", "banks", "real_addresses"]
 
def write_csv(dannie, imyafayla):
        with open(imyafayla, "+w", newline="", encoding='UTF-8') as f1:
                fieldnames = getHeaders()
                writer = csv.DictWriter(f1, fieldnames = fieldnames)
                writer.writeheader()
                print("Все записалось", imyafayla)
        f1.close()

def save(file_full_path:str, data_to_save: dict, headers: list):
    with open(file_full_path, mode='a',newline='', encoding="utf-8") as file:
        writer = csv.DictWriter(file, headers)
        writer.writerow(data_to_save)
        file.close()


# write_csv([], csv_name)
# formated_data_getscam.csv
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