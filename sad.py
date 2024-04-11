
from flask import Flask, request
import requests

app = Flask(name)

# Здесь нужно указать ваш токен телеграм бота
TELEGRAM_BOT_TOKEN = '7129981759:AAHsUg_LEBlAFWRopS4uY5APT3TPt2xTYKo'
# Здесь нужно указать ваш chat_id в телеграм (можно узнать у @userinfobot)
TELEGRAM_CHAT_ID = '-4175058493'

# Функция отправки сообщения в Telegram
def send_to_telegram(question):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': f'New question: {question}'
    }
    requests.post(url, data=data)

# Обработка входящих сообщений от GitHub Pages
@app.route('/submit', methods=['POST'])
def submit():
    question = request.form['question']
    send_to_telegram(question)
    return 'Question sent to Telegram!'

if name == 'main':
    app.run(host='0.0.0.0', port=5000)
