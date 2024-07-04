from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import os
import shutil

app = Flask(__name__)

# Укажите путь к каталогам с изображениями
UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'uploads')
IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['IMAGES_FOLDER'] = IMAGES_FOLDER

# Создаем каталоги, если они не существуют
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(IMAGES_FOLDER):
    os.makedirs(IMAGES_FOLDER)

@app.route('/')
def index():
    try:
        # Убедитесь, что каталог существует
        if not os.path.exists(app.config['UPLOAD_FOLDER']):
            return f"Каталог {app.config['UPLOAD_FOLDER']} не существует", 404

        # Получите список файлов в каталоге
        files = os.listdir(app.config['UPLOAD_FOLDER'])
        # Фильтруйте список, чтобы оставить только файлы изображений
        image_files = [file for file in files if file.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif'))]
        return render_template('index.html', images=image_files)
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

@app.route('/images/<filename>')
def display_image(filename):
    try:
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

@app.route('/delete/<filename>', methods=['POST'])
def delete_image(filename):
    try:
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            return redirect(url_for('index'))
        else:
            return f"Файл {filename} не найден", 404
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

@app.route('/upload_all', methods=['POST'])
def upload_all_images():
    try:
        # Получите список файлов в каталоге images
        files = os.listdir(app.config['IMAGES_FOLDER'])
        # Копируйте каждый файл в каталог uploads
        for file in files:
            if file.endswith(('png', 'jpg', 'jpeg', 'bmp', 'gif')):
                src = os.path.join(app.config['IMAGES_FOLDER'], file)
                dst = os.path.join(app.config['UPLOAD_FOLDER'], file)
                shutil.copy(src, dst)
        return redirect(url_for('index'))
    except Exception as e:
        return f"Произошла ошибка: {str(e)}", 500

@app.route('/delete_all_images', methods=['POST'])
def delete_all_images():
    for file in os.listdir(app.config['UPLOAD_FOLDER']):
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file)
        if os.path.isfile(file_path):
            os.remove(file_path)
    return redirect(url_for('index'))

if __name__ == '__main__':
    print(f"Каталог изображений: {app.config['UPLOAD_FOLDER']}")
    app.run(debug=True, host='0.0.0.0', port=5000, ssl_context=('cert.pem', 'key.pem'))