#{"json":{"modelVersionId":null,"tag":null,"authed":true},"meta":{"values":{"modelVersionId":["undefined"],"tag":["undefined"]}}}

import os
import requests

#api civitai token: bf27d4a2e811cd410c03e990e519a2b2
api_token = 'bf27d4a2e811cd410c03e990e519a2b2'
os.environ['CIVITAI_API_TOKEN'] = api_token

# URL для загрузки изображения
url = 'https://civitai.com/api/trpc/post.create'

# Пример данных для отправки
data = {"modelVersionId": 'null', "tag": 'null', "authed": 'true'},
meta = {"values": {"modelVersionId": ["undefined"], "tag": ["undefined"]}}

# Заголовки с токеном аутентификации
headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json'
}

print(f"Отправка запроса на URL: {url} с данными: {data} и заголовками: {headers}")

# Отправка POST-запроса
response = requests.post(url, json=data, headers=headers)

# Проверка статуса ответа
if response.status_code == 200:
    print('POST-запрос выполнен успешно')
    print(response.json())  # Печать ответа сервера
else:
    print(f'Ошибка: {response.status_code} - {response.text}')