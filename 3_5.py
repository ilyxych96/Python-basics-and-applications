'''
3.5.1
Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе
Чикаго с 2001 года по настоящее время.

Одним из атрибутов преступления является его тип – Primary Type.

Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
'''

import csv

frequency = dict()
with open('Crimes.csv') as f:
    csv_reader = csv.reader(f, delimiter=',')
    for row in csv_reader:
        if '2015' in row[2]:
            count = frequency.get(row[5], 0)
            frequency[row[5]] = count + 1

frequency_list = frequency.keys()
for crime in frequency_list:
    print(crime, frequency[crime])

print('MAX Freqently crime: ', max(frequency, key=frequency.get))

'''
3.5.2
Вам дано описание наследования классов в формате JSON.
Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть 
поле name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.

Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется 
явно от одного класса более одного раза.

Для каждого класса вычислите предком скольких классов он является и выведите эту информацию в следующем формате.

<имя класса> : <количество потомков>

Выводить классы следует в лексикографическом порядке.
'''
import json


def turn(dct, par, ret):
    ret.update(dct[par])
    for element in dct[par]:
        ret.update(turn(dct, element, ret))
    return ret


js = json.loads(input())
ans, main = [], {}
for element in js:
    main[element["name"]] = set(element["parents"])
for parent in sorted(main.keys()):
    ans.append(turn(main, parent, set()))
for parent in sorted(main.keys()):
    c = 1
    for element in ans:
        if parent in element:
            c += 1
    print(parent + ' : ' + str(c))



