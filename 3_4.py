'''
3.4.1 Рассмотрим два HTML-документа A и B.
Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. 
внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
Из A можно перейти в B за два перехода если существует такой документ C,
что из A в C можно перейти за один переход и из C в B можно перейти за один переход.

'''
import re
import urllib.request

a = input()
b = input()

def get_links(url):
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.*href="([^"]*)"', mystr)
    except:
        return []
    else:
        return links

def two_steps():
    links1 = get_links(a)

    for link in links1:
        links2 = get_links(link)
        if b in links2:
            return True
    return False

if two_steps():
    print("Yes")
else:
    print("No")
	
	
'''
3.4.2 Вашей программе на вход подается ссылка на HTML файл.
Вам необходимо скачать этот файл, затем найти в нем все ссылки
вида <a ... href="..." ... > и вывести список сайтов, на 
которые есть ссылка.

Сайтом в данной задаче будем называть имя домена вместе с именами 
поддоменов. То есть, это последовательность символов, которая следует 
сразу после символов протокола, если он есть, до символов порта или 
пути, если они есть, за исключением случаев с относительными ссылками вида
<a href="../some_path/index.html">.

Сайты следует выводить в алфавитном порядке.
'''

import re
import urllib.request
from urllib.parse import urlparse

url = input()


def get_links():
    try:
        fp = urllib.request.urlopen(url)
        mybytes = fp.read()
        mystr = mybytes.decode("utf8")
        fp.close()
        links = re.findall(r'<a.+href=[\'"]([^./][^\'"]*)[\'"]', mystr)
    except:
        return []
    else:
        return links


def parser(link):
    parsed_uri = urlparse(link)
    res = parsed_uri.netloc
    try:
        return res[:res.index(':')]
    except:
        return res
    else:
        return res[:res.index(':')]


links = get_links()

unsorted_links = list(map(parser, links))

for link in sorted(list(set(unsorted_links))):
    print(link)



