# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# Press Ctrl+F8 to toggle the breakpoint.
import requests
import os

# Установите API токен
api_token = 'bf27d4a2e811cd410c03e990e519a2b2'
os.environ['CIVITAI_API_TOKEN'] = api_token

if not api_token:
    raise ValueError("Не установлен токен в переменной окружения CIVITAI_API_TOKEN")

# Заголовки с токеном аутентификации
headers = {
    'Authorization': f'Bearer {api_token}'
}

# Укажите URL веб-сайта, куда нужно отправить изображение
url = 'https://civitai.com/api/image-upload'

# Укажите путь к изображению, которое нужно отправить
image_path = 'images/new2.png'

if __name__ == '__main__':
    # Откройте изображение в бинарном режиме
    with open(image_path, 'rb') as image_file:
        # Подготовьте данные для отправки
        files = {'file': ('new2.png', image_file, 'image/png')}

        print(f'Изображение успешно найдено: {image_file}')

        # Отправка POST-запроса
        response = requests.post(url, files=files, headers=headers)

    # Проверьте статус ответа
    if response.status_code == 200:
        print(f'Изображение успешно отправлено: {response.status_code}')
        print(response.json())  # Печать ответа сервера
    else:
        print(f'Ошибка отправки изображения: {response.status_code}')
        print(response.text)  # Печать текста ошибки для диагностики