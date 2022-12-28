import telebot
from telebot import types  # для указание типов
from PIL import Image
import promo_code as p
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')
with open('promo_code.txt', 'r', encoding='utf-8') as file:
    txt = file.readlines()


@bot.message_handler(commands=['start', "Главное меню Бота"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Акции #ЭTOPIZZA")
    btn2 = types.KeyboardButton("Скидки #ЭTOPIZZA")
    btn3 = types.KeyboardButton("Промокоды")
    btn4 = types.KeyboardButton("Меню")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=markup)

@bot.message_handler(commands=["Меню #ЭTOPIZZA"])
def menu(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1_1 = types.KeyboardButton("Напитки")
    btn2_1 = types.KeyboardButton("Десерты")
    btn3_1 = types.KeyboardButton("Главное меню Бота")
    markup1.add(btn1_1, btn2_1, btn3_1)
    bot.send_message(message.from_user.id, 'Меню Это пицца', reply_markup=markup1)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Акции #ЭTOPIZZA":
        with open('promotion.txt', 'r', encoding='utf-8') as file:
            text=file.readlines()
            for i in text:
                bot.send_message(message.from_user.id, i.strip())
    elif message.text == "Скидки #ЭTOPIZZA":
        with open('discount.txt', 'r', encoding='utf-8') as file:
            text=file.readlines()
            for i in text:
                bot.send_message(message.from_user.id, i.strip())
    if message.text == "Меню #ЭTOPIZZA":
        menu(message)
    elif message.text == "Главное меню Бота":
        start(message)
    elif message.text == "Промокоды":
        p.choise_inpt(message)
    elif 'ПРОМОКОД' in message.text.upper():
        p.prm_cd(message)





bot.polling(none_stop=True, interval=1)
  #for commit
