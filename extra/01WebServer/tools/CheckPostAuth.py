import requests
import os

# Получите токен из переменной окружения
# token = os.getenv('CIVITAI_API_TOKEN')

url = 'https://civitai.com/api/image-upload'
data = {'param1': 'value1', 'param2': 'value2'}

headers = {
    'Authorization': f'Bearer {token}',
    'Content-Type': 'application/json'
}

response = requests.post(url, json=data, headers=headers)

if response.status_code == 200:
    print('POST-запрос выполнен успешно')
else:
    print(f'Ошибка: {response.status_code} - {response.text}')