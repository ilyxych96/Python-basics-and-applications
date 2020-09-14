'''
Реализуйте программу, которая будет вычислять количество различных объектов в списке.
Два объекта a и b считаются различными, если a is b равно False.
'''
mn = []
for obj in objects:
    if obj not in mn:
        mn.append(obj)
print(len(mn))