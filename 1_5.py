'''
1_5_1
Реализуйте класс MoneyBox, для работы с виртуальной копилкой.

Каждая копилка имеет ограниченную вместимость, которая выражается 
целым числом – количеством монет, которые можно положить в копилку.
 Класс должен поддерживать информацию о количестве монет в копилке,
 предоставлять возможность добавлять монеты в копилку и узнавать, 
 можно ли добавить в копилку ещё какое-то количество монет, не 
 превышая ее вместимость.

'''

class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.amount = 0
 
    def can_add(self, v):
        self.adding = v
        if self.adding + self.amount <= self.capacity:
            return True
        else:
            return False
 
    def add(self, v):
        self.amount += v
		
'''
1_5_2
Вам дается последовательность целых чисел и вам нужно ее обработать 
и вывести на экран сумму первой пятерки чисел из этой последовательности,
 затем сумму второй пятерки, и т. д.

Но последовательность не дается вам сразу целиком. С течением времени 
к вам поступают её последовательные части. Например, сначала первые три
 элемента, потом следующие шесть, потом следующие два и т. д.

Реализуйте класс Buffer, который будет накапливать в себе элементы 
последовательности и выводить сумму пятерок последовательных элементов 
по мере их накопления.

Одним из требований к классу является то, что он не должен хранить в 
себе больше элементов, чем ему действительно необходимо, т. е. он не 
должен хранить элементы, которые уже вошли в пятерку, для которой была 
выведена сумма.
'''	
	
class Buffer:

    def __init__(self):
        self.current_part = []

    def add(self, *a):
        self.current_part.extend(a)
        while len(self.current_part) >= 5:
            print(sum(self.current_part[0:5]))
            self.current_part = self.current_part[5:]

    def get_current_part(self):
        return self.current_part
