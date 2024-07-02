from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'Нет файла в запросе'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'Файл не выбран'}), 400

    if file:
        # Сохраните файл
        file.save(f'uploads/{file.filename}')
        return jsonify({'success': 'Файл успешно загружен'}), 200

if __name__ == '__main__':
    # Замените 'cert.pem' и 'key.pem' на ваши файлы сертификата и ключа
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))