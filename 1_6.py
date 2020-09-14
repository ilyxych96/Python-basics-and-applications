'''
1_6_1
Вам дано описание наследования классов в следующем формате.
<имя класса 1> : <имя класса 2> <имя класса 3> ... <имя класса k>
Это означает, что класс 1 отнаследован от класса 2, класса 3, и т. д.

Класс A является предком класса B, если
A = B;
A - прямой предок B
существует такой класс C, что C - прямой предок B и A - предок C

Вам необходимо отвечать на запросы, является ли один класс предком другого класса

'''

classes = {}

def add_class(classes, class_name, parents):
    if class_name not in classes:
        classes[class_name] = []
    classes[class_name].extend(parents)
    for parent in parents:
        if parent not in classes:
            classes[parent] = []

def found_path(classes, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in classes:
        return None
    for node in classes[start]:
        if node not in path:
            newpath = found_path(classes, node, end, path)
            if newpath: return newpath
    return None

def answer(classes, parent, child):
    if not(parent or child) in classes or not found_path(classes, child, parent):
        return 'No'
    return 'Yes'

n = int(input())
for _ in range(n):
    class_description = input().split()
    class_name = class_description[0]
    class_parents = class_description[2:]
    add_class(classes, class_name, class_parents)

q = int(input())
for _ in range(q):
    question = input().split()
    parent = question[0]
    child = question[1]
    print(answer(classes, parent, child))


'''
1_6_2

Реализуйте структуру данных, представляющую собой расширенную структуру стек. 
Необходимо поддерживать добавление элемента на вершину стека, удаление с вершины стека,
 и необходимо поддерживать операции сложения, вычитания, умножения и целочисленного деления.

Операция сложения на стеке определяется следующим образом. Со стека снимается верхний 
элемент (top1), затем снимается следующий верхний элемент (top2), и затем как результат 
операции сложения на вершину стека кладется элемент, равный top1 + top2.

Аналогичным образом определяются операции вычитания (top1 - top2), умножения (top1 * top2) 
и целочисленного деления (top1 // top2).

Реализуйте эту структуру данных как класс ExtendedStack, отнаследовав его от 
стандартного класса list.

'''
class ExtendedStack(list):
    def sum(self):
        self.append(self.pop()+self.pop())
        # операция сложения

    def sub(self):
        self.append(self.pop()-self.pop())
        # операция вычитания

    def mul(self):
        self.append(self.pop()*self.pop())
        # операция умножения

    def div(self):
        self.append(self.pop()//self.pop())
        # операция целочисленного деления
		
'''
1_6_3
Одно из применений множественного наследование – расширение функциональности класса 
каким-то заранее определенным способом. Например, если нам понадобится логировать 
какую-то информацию при обращении к методам класса.

Рассмотрим класс Loggable:

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))
		
У него есть ровно один метод log, который позволяет выводить в 
лог (в данном случае в stdout) какое-то сообщение, добавляя при этом текущее время.
Реализуйте класс LoggableList, отнаследовав его от классов list и Loggable таким 
образом, чтобы при добавлении элемента в список посредством метода append в лог 
отправлялось сообщение, состоящее из только что добавленного элемента.

'''		
class LoggableList(list, Loggable):
    def append(self, x):
        super(LoggableList, self).append(x)
        self.log(x)
