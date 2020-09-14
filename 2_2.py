'''
В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента 
исходной даты date пройдет число дней, равное days.
'''

import datetime
year, month, day = map(int, input().split())
date = datetime.date(year, month, day)
newday = date + datetime.timedelta(days=int(input()))
print(newday.year, newday.month, newday.day)
    