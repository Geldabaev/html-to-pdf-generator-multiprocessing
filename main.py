import time
import sys
import aspose.words as aw
import multiprocessing
import requests
from flask import Flask, render_template
import asyncio

app = Flask(__name__)

# введите значения через запятую
answer = ['Первое значение', 'Второе значение', 'Третье значение']


@app.route('/')
def index():
    return render_template('index.html', answer=answer)


def save_html():
    print("Генерация html")
    r = requests.get('http://127.0.0.1:5000')
    html = r.text
    with open('test.html', 'w', encoding='utf8') as f:
        f.write(html)


def generate_label():
    time.sleep(5)
    save_html()
    print("Конвертация в pdf")
    doc = aw.Document("test.html")
    doc.save("file.pdf")
    print("Готово! Нажмите CTRL + C и Заберите файл file.pdf!")


def run_flask():
    print('Запуск сервера')
    app.run(debug=True)


if __name__ == '__main__':
    multiprocessing.Process(target=generate_label).start()
    run_flask()
