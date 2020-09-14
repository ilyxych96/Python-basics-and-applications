'''
Реализуйте программу, которая будет эмулировать работу с пространствами имен. 
Необходимо реализовать поддержку создания пространств имен и добавление в них переменных.

В данной задаче у каждого пространства имен есть уникальный текстовый идентификатор – его имя.

Вашей программе на вход подаются следующие запросы:

create <namespace> <parent> –  создать новое пространство имен с именем <namespace> внутри пространства <parent>
add <namespace> <var> – добавить в пространство <namespace> переменную <var>
get <namespace> <var> – получить имя пространства, из которого будет взята 
переменная <var> при запросе из пространства <namespace>, или None, если такого пространства не существует
'''
class nmspc(list):
    names = {"global": ["None"],"None":[]}
    def create(self, space, parent):
        self.names[parent].append(space)
        self.names[space] = [parent]
    def add(self, space, var):
        self.names[space].append(var)
    def get(self, space, var):
        if space == "None":
            return
        if var in self.names[space]:
            print(space)
            return
        elif self.names[space][0] != "None":
            self.get(self.names[space][0], var)
            return
        else:
            print("None")
        return
		
		
a = nmspc()
n = int(input())
for i in range(n):
    s = input().split()
    if s[0] == "add":
        a.add(s[1], s[2])
    elif s[0] == "create":
        a.create(s[1], s[2])
    else:
        a.get(s[1], s[2])


