import telebot
from telebot import types
from PIL import Image
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')

def discount(message):
    with Image.open('discount\Скидка в инстаграмме.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидка в инстаграмме*',parse_mode="Markdown")
    with Image.open('discount\Скидка День семьи.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидка День семьи*',parse_mode="Markdown")
    with Image.open('discount\Скидка на заказ от 50 руб, от 100 руб.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидка на заказ от 50 руб, от 100 руб*',parse_mode="Markdown")
    with Image.open('discount\Скидка на напиток в свою кружку 20%.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидка на напиток в свою кружку 20%*',parse_mode="Markdown")
    with Image.open('discount\Скидка 7% клиентам по номеру телефона и ФИ.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидка 7% клиентам по номеру телефона и ФИ*',parse_mode="Markdown")
    with Image.open('discount\Скидки работникам пиццерии.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидки работникам пиццерии*',parse_mode="Markdown")
    with Image.open('discount\Скидка 100%. Урегулирование конфликтов.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Скидка 100%. Урегулирование конфликтов*',parse_mode="Markdown")
