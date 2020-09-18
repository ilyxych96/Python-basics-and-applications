'''
3.3.1
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве подстроки хотя бы два раза.
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    out = re.findall('cat', line)
    if len(out) > 1:
        print(line)

'''
3.3.2
Вам дана последовательность строк.
Выведите строки, содержащие "cat" в качестве слова.
'''
# put your python code here
import sys
import re

template = r"\bcat\W?\b"

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(template, line):
        print(line)

'''
3.3.3
Вам дана последовательность строк.
Выведите строки, содержащие две буквы "z﻿", между которыми ровно три символа.
'''
import sys
import re

template = r"z\w\w\wz"

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(template, line):
        print(line)

'''
3.3.4
Вам дана последовательность строк.
Выведите строки, содержащие обратный слеш "\﻿".
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.findall(r'\\', line):
        print(line)

'''
3.3.5
Вам дана последовательность строк.
Выведите строки, содержащие слово, состоящее из двух одинаковых частей (тандемный повтор).
'''
import sys
import re

template = r"\b(\w+\B)\1\b"

for line in sys.stdin:
    line = line.rstrip()
    if re.match(template, line):
        print(line)

'''
3.3.6
Вам дана последовательность строк.
В каждой строке замените все вхождения подстроки "human" на подстроку "computer"﻿ и выведите полученные строки.
'''
import sys
import re

for line in sys.stdin:
    line = line.rstrip()
    if re.sub('human', 'computer', line):
        print(re.sub('human', 'computer', line))

'''
3.3.7
Вам дана последовательность строк.
В каждой строке замените первое вхождение слова, состоящего только из латинских букв "a" 
(регистр не важен), на слово "argh".
'''
import sys
import re

template = r'\b[aA]+\b'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(template, "argh", line, count=1, flags=re.IGNORECASE))

'''
3.3.7
Вам дана последовательность строк.
В каждой строке поменяйте местами две первых буквы в каждом слове, состоящем хотя бы из двух букв.
Буквой считается символ из группы \w.
'''
import sys
import re

template = r'\b(\w)(\w)'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(template, r'\2\1',line))

'''
Вам дана последовательность строк.
В каждой строке замените все вхождения нескольких одинаковых букв на одну букву.
Буквой считается символ из группы \w.
'''
import sys
import re

template = r'(\w)(\1+)'

for line in sys.stdin:
    line = line.rstrip()
    print(re.sub(template, r'\1', line))
