
from flask import Flask, request, render_template
import requests

app = Flask(__name__)

# Здесь нужно указать ваш токен телеграм бота
TELEGRAM_BOT_TOKEN = '7129981759:AAHsUg_LEBlAFWRopS4uY5APT3TPt2xTYKo'
# Здесь нужно указать ваш chat_id в телеграм (можно узнать у @userinfobot)
TELEGRAM_CHAT_ID = '-4175058493'
# Здесь нужно указать URL вашего Flask приложения
FLASK_APP_URL = 'http://127.0.0.1:5000'

def set_webhook():
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/setWebhook'
    params = {
        'url': FLASK_APP_URL + '/' + TELEGRAM_BOT_TOKEN
    }
    response = requests.post(url, params=params)  # Используем POST вместо GET
    print(response.json())


# Обработка главной страницы
@app.route('/')
def index():
    return render_template('index.html')

# Обработка отправки формы
@app.route('/submit', methods=['POST'])
def submit():
    question = request.form['question']
    send_to_telegram(question)
    return 'Question sent to Telegram!'

# Функция отправки сообщения в Telegram
def send_to_telegram(question):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': f'New question: {question}'
    }
    requests.post(url, data=data)

# Обработка входящих сообщений от Telegram
@app.route(f'/{TELEGRAM_BOT_TOKEN}', methods=['POST'])
def telegram_webhook():
    update = request.json
    chat_id = update['message']['chat']['id']
    message_text = update['message']['text']
    send_reply(chat_id, message_text)
    return 'OK'

# Функция отправки ответа в Telegram
def send_reply(chat_id, message_text):
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': f'You said: {message_text}'
    }
    requests.post(url, data=data)

if __name__ == '__main__':
    set_webhook()  # Установка веб-хука перед запуском Flask приложения
    app.run(debug=True)
