import requests

url = 'https://civitai.com/user/denfrosty/images' #https://example.com/path #https://civitai.com/posts/create
data = {'param1': 'value1', 'param2': 'value2'}

response = requests.post(url, data=data)

# Проверка ответа
if response.status_code == 200:
    print('POST-запрос выполнен успешно')
else:
    print(f'Ошибка: {response.status_code}')