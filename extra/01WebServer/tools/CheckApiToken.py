import os
import requests

# Получите токен из переменной окружения
token = os.getenv('CIVITAI_API_TOKEN')

if not token:
    raise ValueError("Не установлен токен в переменной окружения CIVITAI_API_TOKEN")

url = 'https://civitai.com/posts/create'
data = {'param1': 'value1', 'param2': 'value2'}

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print(f'Token-used Bearer: {token}')
    print('POST-запрос выполнен успешно')
else:
    print(f'Ошибка: {response.status_code} - {response.text}')