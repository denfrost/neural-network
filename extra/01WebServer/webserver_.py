from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os

app = Flask(__name__)

# Укажите путь к каталогу с изображениями
IMAGE_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

# Создаем каталог, если он не существует
if not os.path.exists(IMAGE_FOLDER):
    os.makedirs(IMAGE_FOLDER)

@app.route('/')
def index():
    try:
        # Убедитесь, что каталог существует
        if not os.path.exists(app.config['IMAGE_FOLDER']):
            return f"Каталог {app.config['IMAGE_FOLDER']} не существует", 404

        # Получите список файлов в каталоге
        files = os.listdir(app.config['IMAGE_FOLDER'])
        # Фильтруйте список, чтобы оставить только файлы изображений
        image_files = [file for file in files if file.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        return render_template('index.html', images=image_files)
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

@app.route('/images/<filename>')
def display_image(filename):
    try:
        return send_from_directory(app.config['IMAGE_FOLDER'], filename)
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

@app.route('/delete/<filename>', methods=['POST'])
def delete_image(filename):
    try:
        file_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return redirect(url_for('index'))
        else:
            return f"Файл {filename} не найден", 404
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

if __name__ == '__main__':
    print(f"Каталог изображений: {app.config['IMAGE_FOLDER']}")
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))