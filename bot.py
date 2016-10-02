# -*- coding: utf-8 -*-
# задание: настройте изображение профиля вашего бота

import config
import telebot
from telebot import types
import urllib

bot = telebot.TeleBot(config.token)


url = 'http://www.1366x768.ru/3D/190/abstraction-wallpaper-1366x768.jpg'
marmot = 'http://www.factroom.ru/facts/wp-content/uploads/2011/02/surok.jpg'
cat = 'http://fit4brain.com/wp-content/uploads/2014/05/cat.jpg'


@bot.message_handler(commands=['help'])
def send_help(message):
    msg = bot.send_message(message.chat.id, "Список доступных команд: "
                                            "/start, /help, /surikat, /photo ")


@bot.message_handler(commands=['surikat', 'сурикатик', 'капибашка'])
def send_suri(message):
    msg = bot.send_message(message.chat.id, 'Привет, Паша! Не грусти!')


@bot.message_handler(commands=['photo'])
def send_photo(message):
    msg = bot.send_photo(message.chat.id, url, "photo")


@bot.message_handler(commands=['start'])
def send_info(message):
    msg = bot.send_message(message.chat.id, 'Привет! я твой бот. Начнем?')


#@bot.message_handler(commands=['Да', 'lf', 'yes', 'да'])
@bot.message_handler(content_types='text')
def send_msg(message):
    if message.text == 'да' or message.text == 'Да':
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, selective=True)
        markup.add('Открой меня!', 'Нажми на меня!')
        msg = bot.reply_to(message, 'Итак...', reply_markup=markup)
        bot.register_next_step_handler(msg, process_step)


def process_step(message):
    chat_id = message.chat.id
    if message.text == 'Открой меня!':
        msg = bot.send_message(message.chat.id, 'Меня зовут Кот, просто Кот. Я живу здесь')
        msg = bot.send_photo(message.chat.id, cat, "Cat")
    if message.text == 'Нажми на меня!':
        msg = bot.send_message(message.chat.id, 'Меня зовут Сурок и я хочу спать')
        msg = bot.send_photo(message.chat.id, marmot, "Marmot")
    msg = bot.reply_to(message, 'Выполнено', reply_markup=types.ReplyKeyboardHide())


#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
#    bot.reply_to(message, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
