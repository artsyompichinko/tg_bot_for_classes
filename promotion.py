import telebot
from telebot import types
from PIL import Image
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')
def promotions(message):
    with Image.open('promotion\Акция день рождение!.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Акция день рождение!*',parse_mode="Markdown")
    with Image.open('promotion\Акция на 10 минут в инстаграме.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Акция на 10 минут в инстаграме*',parse_mode="Markdown")
    with Image.open('promotion\Акция напиток в подарок.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Акция напиток в подарок*',parse_mode="Markdown")
    with Image.open('promotion\Акция Х2.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Акция Х2*',parse_mode="Markdown")
    with Image.open('promotion\Бесплатный 5-й напиток, бесплатный 10-й напиток + чизкейк (КОФЕСОБИРАЛКИ).jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Бесплатный 5-й напиток, бесплатный 10-й напиток + чизкейк (КОФЕСОБИРАЛКИ)*',parse_mode="Markdown")