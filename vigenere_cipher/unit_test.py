import json

from vigenere_cipher import decrypt_message, encrypt_message,is_alphabet

import pathlib
path = pathlib.Path(__file__).parent.resolve()


test_filename = path / 'unit_test.json'    

def open_json(filename:str):
    with open(filename,'r',encoding='utf-8') as json_file:
        return json.load(json_file)

def save_json(filename: str,data: any):
    with open(filename, "w",encoding='utf-8') as json_file:
        json.dump(data, json_file)

def generate_cipher(filename):
    """Do generate cipher and save json"""

    json_data = open_json(filename)

    for data in json_data:
        key = data['key']
        messages = data['messages']
        data['ciphers'] = []
        for message in messages:
            data['ciphers'].append(encrypt_message(message,key))
    
    return json_data

#TODO:test decorator

def test_encrypt_decrypt(key:str, messages:list[str]):
    for m in messages:
        assert m == decrypt_message(encrypt_message(m,key),key)

def test_is_alphabet():
    test_x = ['a','',' ','1','a3']
    test_y = [True, False, False,False, False]
    for i,x in enumerate(test_x):
        assert test_y[i] == bool(is_alphabet(x)), (x, bool(is_alphabet(x)))

if __name__ == "__main__":
    test_json = open_json(test_filename)
    
    test_is_alphabet()

    for unit in test_json:
        key = unit['key']
        messages = unit['messages']
        test_encrypt_decrypt(key,messages)

    print('Done')