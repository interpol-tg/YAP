import requests
from urllib import request, parse
from json import loads
from bs4 import BeautifulSoup
import telebot


TOKEN = '5617922716:AAFdQh1jljdM02177UKpNxpElhQe15bHUqU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет, отправь команду /get *ключевое слово* *количество*")


@bot.message_handler(commands=['get'])
def send_welcome(message):
    print(message.text.split(' '))
    link = message.text.split(' ')[1]
    link2 = int(message.text.split(' ')[2])
    s = requests.session()
    s.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0'})
    r = s.get(
        f'https://yandex.ru/images/search?text={link}&from=tabbar&source-serpid=y_5FcX5ld3Qq6YXCeyOKIQ&noreask=1&nomisspell=1')
    for i in range(1, link2):
        bot.send_message(message.chat.id, r.text.split('img class="serp-item__thumb justifier__thumb"')[i].split('data-error-handler=')[0])

bot.polling(none_stop=True)


