'''
3.6.1 В этой задаче вам необходимо воспользоваться API сайта numbersapi.com

Вам дается набор чисел. Для каждого из чисел необходимо узнать, существует ли интересный
математический факт об этом числе.

Для каждого числа выведите Interesting, если для числа существует интересный факт, и Boring иначе.
Выводите информацию об интересности чисел в таком же порядке, в каком следуют числа во входном файле.
'''
'''import requests

dataset = 'dataset_24476_3.txt'
with open(dataset) as f:
    for number in f:
        reference = 'http://numbersapi.com/' + str(number.rstrip()) + '/math?json=true'
        def get_html(URL, params=None):
            headers = []
            response = requests.get(URL, headers=headers, params=params, allow_redirects=True)
            return response

        status = get_html(reference)
        status = status.text.split(',')[2].split(' ')[2]
        if status == 'true':
            print('Interesting')
        else:
            print('Boring')
'''
'''
3.6.2 В этой задаче вам необходимо воспользоваться API сайта artsy.net

API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.

В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).

Вам даны идентификаторы художников в базе Artsy.
Для каждого идентификатора получите информацию о имени художника и годе рождения.
Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый 
год рождения, выведите их имена в лексикографическом порядке.

Работа с API Artsy

Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, 
для получения доступа к API необходимо зарегистрироваться в проекте, создать свое приложение, и 
получить уникальный ключ (или токен), и в дальнейшем все запросы к API осуществляются при помощи этого ключа.

Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации 
к API https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, 
создать приложение, и получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.

После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, 
как можно выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.

'''
import requests
import json

client_id = '1b09d5aefdd4dc74d5b7'
client_secret = '22adaf27a3a3b1bea55991c13798e4e4'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
j = json.loads(r.text)

# достаем токен
token = j["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
artist_dict = dict()
with open('artists.txt', encoding="'utf-8'") as f:
    for artist in f:
        url = 'https://api.artsy.net/api/artists/' + str(artist.rstrip())
        r = requests.get(url, headers=headers)
        j = json.loads(r.text)
        artist_dict.update([(j['sortable_name'], j['birthday'])])

sorted_by_years = sorted(artist_dict.items(), key=lambda x: (x[1], x[0]))
for artist in sorted_by_years:
    print(artist[0])