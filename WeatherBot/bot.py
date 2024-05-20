import telebot
import requests
import json

bot = telebot.TeleBot('7143647141:AAFYmigpj88MKWqqd7kXFQT7G_McQsT-HoA')
API = '9b6486149040c51e7fb61b95f0557c08'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Enter City Name.')

@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()
    tmp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if tmp.status_code == 200:
        data = json.loads(tmp.text)
        temp = data["main"]["temp"]
        for weather in data["weather"]:
            description = weather["main"]
        bot.send_message(message.chat.id,f'Weather in {message.text} Now is {temp} °C {description}')
    else:
        bot.send_message(message.chat.id,f'Non existent City')


bot.polling(none_stop=True)