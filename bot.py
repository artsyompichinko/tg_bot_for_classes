import telebot
from telebot import types # для указание типов
from PIL import Image
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')

@bot.message_handler(commands=['start',"Главное меню Бота"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Действующие акции")
    btn2 = types.KeyboardButton("Промокоды")
    btn3 = types.KeyboardButton("")
    btn4 = types.KeyboardButton("Меню #ЭTOPIZZA")
    markup.add(btn1, btn2,btn3, btn4)
    bot.send_message(message.from_user.id, 'Стартовое меню', reply_markup=markup)

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
    if message.text == "Действующие акции":
        with open('promotion', 'r', encoding='utf-8') as file:
            text=file.readlines()
            for i in text:
                bot.send_message(message.from_user.id, i.strip())
        with Image.open('birthday_prom.jpg') as img:
            bot.send_photo(message.from_user.id, img)
    if message.text == "Меню #ЭTOPIZZA":
        a = telebot.types.ReplyKeyboardRemove()  # удаление кнопок
        menu(message)
    if message.text == "Главное меню Бота":
        a = telebot.types.ReplyKeyboardRemove()  # удаление кнопок
        start(message)

bot.polling(none_stop=True, interval=1)
#for commit
