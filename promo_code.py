import telebot
from telebot import types
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')
def choise_inpt(message):
    with open('promo_code.txt', 'r', encoding='utf-8') as file:
        txt = file.readlines()
    if message.text=='Промокоды':
        for i in txt:
            bot.send_message(message.from_user.id, i.strip())


def prm_cd(message):
    with open('promo_code.txt', 'r', encoding='utf-8') as file:
        txt = file.readlines()
    answer=(any(map(lambda x: True if x.strip().upper() in message.text.upper() else False,txt)))
    if answer:
        bot.send_message(message.from_user.id, f'Промокод  {message.text.upper()[8:]}  действует!')
    else:
        bot.send_message(message.from_user.id, f'У нас такого промокода нет!')











