import requests
import json
import csv
import os

class OwnException(Exception):
    def __init__(self, message: str, finish_script: bool):
        super().__init__(message)
        self.finish_script = finish_script

def sendRequest(some_url, access_token: str, secret_token: str, phone: str) -> str:
    #headers ={'Content-type': 'application/json'}
    #json_to_send = {'accessToken': access_token, 'secret_token': secretToken, 'telephone': phone}
    #response = requests.post(some_url, headers=headers, json=json_to_send)
    #if response.status_code == 200:
        #return response.text
    #else:
        #raise OwnException('Status code is: ' + str(response.status_code), False)
    #допустим что то отправили и получили
    json_str = '{"resultCode":0,"resultMessage":"success","operationToken":"33d1571389264781a38c29ac3fdc73fc","resultList":[{"firstName":"САЖИНА","lastName":"НАТАША","middleName":null,"telephone":"9501027270","car":null,"passport":null,"dayBirth":null,"monthBirth":null,"yearBirth":null,"snils":null,"inn":null,"base":"ТЕЛЕФОНЫ РФ 2021 NB","id":7862551065,"information":{"Имя контакта":"Наташа Сажина","IMEI связи":"","Последнее обновление":"2021-04-26 23:33:20+00","Связь с номером":"79500843633","Платформа связи":""}},{"firstName":"НАТАЛЬЯ","lastName":"САДОВОД","middleName":null,"telephone":"9501027270","car":null,"passport":null,"dayBirth":null,"monthBirth":null,"yearBirth":null,"snils":null,"inn":null,"base":"ТЕЛЕФОНЫ РФ 2021 NB","id":7551735910,"information":{"Имя контакта":"Садовод Наталья","IMEI связи":"","Последнее обновление":"2021-01-24 06:18:01+00","Связь с номером":"79086433909","Платформа связи":""}}]}'
    print(json_str[4810: 4850])
    return json_str

def jsonDictRepresentation(json_str: str) -> dict:
    json_dict = json.loads(json_str)
    result_code = json_dict['resultCode']
    if result_code != 0:
        raise OwnException('ResultCode is not success: ' + str(result_code), False,)
    else:
        return json_dict

def getHeaders():
    return ["operationToken","telephone","firstName","lastName","middleName","car","passport","dayBirth","monthBirth","yearBirth","snils","inn","base","id","information","error"]

def createFile(file_full_path: str) -> bool:
    try:
        with open(file_full_path, mode='w', encoding='UTF-8') as file:
            csv_headers = getHeaders()
            dw = csv.DictWriter(file, delimiter=';', fieldnames=csv_headers)
            dw.writeheader()
            file.close()
    except RuntimeError as e:
        print(e.message)
        print('Something wrong with creating file. Raise ownException to finish script')
        raise OwnException('Something wrong with creating file.', true)

def saveWithResultList(file_full_path:str, data_to_save: dict, result_list_of_dicts: list):
    for elem in result_list_of_dicts:
        print(elem)
        for key, value in elem.items():
            if value != None:
                data_to_save[key] = value
            else:
                data_to_save[key] = ''
        save(file_full_path, data_to_save)
    
def save(file_full_path:str, data_to_save: dict):
    with open(file_full_path, mode='a', encoding='UTF-8') as file:
        csv_headers = getHeaders()
        writer = csv.DictWriter(file, delimiter=';', fieldnames=csv_headers)
        writer.writerow(data_to_save)
        file.close()
        
def setBlankValues(data_to_save: dict):
    headers = getHeaders()
    for value in headers:
        data_to_save[value] = ''

def saveToFile(file_full_path: str, json_dict: dict, phone: str):
    data_to_save = {}
    data_to_save['operationToken'] = json_dict['operationToken']
    data_to_save['telephone'] = phone
    try:
        if not os.path.exists(file_full_path):
            createFile(file_full_path)
        if len(json_dict['resultList']) == 0:
            setBlankValues(data_to_save)
            save(data_to_save)
        else:
            saveWithResultList(file_full_path, data_to_save, json_dict['resultList'])
    except OwnException as e:
        print(e.message)
        if not os.path.exists(file_full_path):
            data_to_save['error'] = 'error'
            save(file_full_path, data_to_save)
        raise e

def gettingPhonesFromFile(fileName: str) -> list:
    print('do something')
    return ['9501027270', '9501027270']

file_path = '/Users/knapptan/Desktop/IDX_work/sravnenie_servisov/sravnenie_v2'
result_file_special_check = 'specialCheckResult.csv'
some_url = 'url'
access_token = ''
secret_token = ''

phone_list: list = gettingPhonesFromFile('fileNameWithPhones')
for phone in phone_list:
    try:
        body_as_json_text:str = sendRequest(some_url, access_token, secret_token, phone)
    
        json_dict:dict = jsonDictRepresentation(body_as_json_text)

        file_full_path = file_path + result_file_special_check

        saveToFile(file_full_path, json_dict, phone)
    except OwnException as e:
        if e.finish_script:
            break
        print('Continue getting result')


