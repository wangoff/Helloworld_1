import modul
import requests

#имя = input('введи имя ')
#возраст = int(input('введи возраст '))
#modul.приветствие(имя)
#msg = modul.проверкавозраста(возраст)
#print (msg)

response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())
