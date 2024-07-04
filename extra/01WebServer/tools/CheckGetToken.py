import os
import requests

auth_url = 'https://civitai.com/auth/token'
auth_data = {
    'username': 'your_username',
    'password': 'your_password'
}

auth_response = requests.post(auth_url, data=auth_data)

if auth_response.status_code == 200:
    token = auth_response.json().get('access_token')
    # Используйте полученный токен для последующих запросов
else:
    print(f'Ошибка получения токена: {auth_response.status_code} - {auth_response.text}')