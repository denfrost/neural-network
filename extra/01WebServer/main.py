# This is a sample Python script.
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
# Press Ctrl+F8 to toggle the breakpoint.

import requests
from requests.adapters import HTTPAdapter
import ssl

class SSLAdapter(HTTPAdapter):
    def init_poolmanager(self, *args, **kwargs):
        context = ssl.create_default_context()
        context.set_ciphers('DEFAULT:@SECLEVEL=1')
        kwargs['ssl_context'] = context
        return super(SSLAdapter, self).init_poolmanager(*args, **kwargs)

# Укажите URL веб-сайта, куда нужно отправить изображение
url = 'https://localhost:5000/upload'

# Укажите путь к изображению, которое нужно отправить
image_path = 'images/1.png'

# Укажите путь к файлу с сертификатом
cert_path = 'cert.pem'

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Откройте изображение в бинарном режиме
    with open(image_path, 'rb') as image_file:
        # Подготовьте данные для отправки
        files = {'file': image_file}

        # Создайте сессию с адаптером SSL
        session = requests.Session()
        session.mount('https://', SSLAdapter())
        # Отправьте POST-запрос с проверкой сертификата (используйте verify=False для тестирования с самоподписанным сертификатом)
        response = requests.post(url, files=files, verify=cert_path)

    # Проверьте статус ответа
    if response.status_code == 200:
        print('Изображение успешно отправлено')
    else:
        print(f'Ошибка отправки изображения: {response.status_code}')
