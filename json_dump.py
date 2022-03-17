import json

numbers = [3,4,5,12,34,55,66,77]

file = 'numbers.json'
with open(file,'w') as fb:
    json.dump(numbers,fb)
print(3*'-----------------------')    
print('Reading the json file: ')

with open(file,'r') as fr:
    numbers2 = json.load(fr)
    
print(numbers2)