'''
2_1_1
Вашей программе будет доступна функция foo, которая может бросать исключения.

Вам необходимо написать код, который запускает эту функцию, затем ловит исключения 
ArithmeticError, AssertionError, ZeroDivisionError и выводит имя пойманного исключения.
'''
try:
    foo()
except AssertionError:
    print("AssertionError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except ArithmeticError:
    print("ArithmeticError")
	
'''
2_1_2
Вам дано описание наследования классов исключений в следующем формате.
<имя исключения 1> : <имя исключения 2> <имя исключения 3> ... <имя исключения k>
Это означает, что исключение 1 наследуется от исключения 2, исключения 3, и т. д.

Костя посмотрел на этот код и указал Антону на то, что некоторые исключения можно 
не ловить, так как ранее в коде будет пойман их предок. Но Антон не помнит какие 
исключения наследуются от каких. Помогите ему выйти из неловкого положения и 
напишите программу, которая будет определять обработку каких исключений можно 
удалить из кода.
'''
exceptions = {}
throwed_exceptions = []

def found_path(exceptions, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in exceptions:
        return []
    for node in exceptions[start]:
        if node not in path:
            newpath = found_path(exceptions, node, end, path)
            if newpath: return newpath
    return []

n = int(input())
for _ in range(n):
    inpt = input().split()
    child = inpt[0]
    parents = inpt[2:]
    exceptions[child] = parents

m = int(input())
for _ in range(m):
    throwing = input()
    for throwed_exception in throwed_exceptions:
        if len(found_path(exceptions, throwing, throwed_exception)) > 1:
            print(throwing)
            break
    throwed_exceptions.append(throwing)

'''
2_1_3
Реализуйте класс PositiveList, отнаследовав его от класса list, для хранения 
положительных целых чисел.
Также реализуйте новое исключение NonPositiveError.

В классе PositiveList переопределите метод append(self, x) таким образом, 
чтобы при попытке добавить неположительное целое число бросалось исключение 
NonPositiveError и число не добавлялось, а при попытке добавить положительное 
целое число, число добавлялось бы как в стандартный list.

В данной задаче гарантируется, что в качестве аргумента x метода append 
всегда будет передаваться целое число.
'''
	
class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, x):
        if x > 0:
            super(PositiveList, self).append(x)
        else:
            raise NonPositiveError
