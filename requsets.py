import requests

response = requests.get('https://api.github.com')
""" print(response.status_code)  # Код состояния HTTP """
""" print(response.headers)  # Заголовки ответа
print(response.text)  # Текст ответа """

data = response.json()
print(data)
