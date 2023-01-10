import telebot
from telebot import types
from PIL import Image
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')

def coupon_promocode_draw_certificate(message):
    with Image.open('coupon_promocode_draw_certificate\Комбо 4 за 6.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Комбо 4 за 6 *',parse_mode="Markdown")
    with Image.open('coupon_promocode_draw_certificate\Комбо 39.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Комбо 39*',parse_mode="Markdown")
    with Image.open('coupon_promocode_draw_certificate\Семейное комбо.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Семейное комбо*',parse_mode="Markdown")
    with Image.open('coupon_promocode_draw_certificate\Сертификаты.png') as img:
        bot.send_photo(message.from_user.id, img, caption='*Сертификаты*',parse_mode="Markdown")
    with Image.open('coupon_promocode_draw_certificate\Промокоды.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Промокоды*',parse_mode="Markdown")
    with Image.open('coupon_promocode_draw_certificate\Розыгрыш.jpg') as img:
        bot.send_photo(message.from_user.id, img, caption='*Розыгрыш*',parse_mode="Markdown")

