import os
import requests

#api civitai token: bf27d4a2e811cd410c03e990e519a2b2
api_token = 'bf27d4a2e811cd410c03e990e519a2b2'
os.environ['CIVITAI_API_TOKEN'] = api_token

if not api_token:
    raise ValueError("Не установлен токен в переменной окружения CIVITAI_API_TOKEN")

print(f"Используемый токен: {api_token}")

# URL для загрузки изображения
url = 'https://civitai.com/api/image-upload'

# Пример данных для отправки
data = {'param1': 'value1', 'param2': 'value2'}

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