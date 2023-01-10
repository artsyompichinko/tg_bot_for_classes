import telebot
from telebot import types  # для указание типов
import coupon_promocode_draw_certificate as cpdc
import promotion as pr
import discount as d
import job_description as j

bot = telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')

@bot.message_handler ( commands = ['start', "Главное меню Бота"] )
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Акции")
    btn2 = types.KeyboardButton("Скидки")
    btn3 = types.KeyboardButton("Меню")
    btn4 = types. KeyboardButton("Информация для персонала")
    btn5 = types.KeyboardButton("Сертификат, Купон, Розыгрыш, Промокод, Комбо")
    markup.row(btn1, btn2, btn3)
    markup.row(btn4)
    markup.row(btn5)
    bot.send_message(message.from_user.id, 'Главное меню', reply_markup=markup)

@bot.message_handler(commands=["Меню"])
def menu(message):
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1_1 = types.KeyboardButton("Напитки")
    btn2_1 = types.KeyboardButton("Десерты")
    btn3_1 = types.KeyboardButton("Главное меню Бота")
    markup1.add(btn1_1, btn2_1, btn3_1)
    bot.send_message(message.from_user.id, 'Меню Это пицца', reply_markup=markup1)


def info_for_staff(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Чек-листы")
    btn2 = types.KeyboardButton("Скрипты")
    btn3 = types.KeyboardButton("Кассовое оборудование")
    btn4 = types.KeyboardButton("Должностные обязанности")
    btn5 = types.KeyboardButton("Отпуска")
    btn6 = types.KeyboardButton("График")
    btn7 = types.KeyboardButton("Система оплаты труда")
    btn8 = types.KeyboardButton("Руководители")
    btn9 = types.KeyboardButton("Техника безопасности")
    btn10 = types.KeyboardButton("Принципы пиццерии")
    btn11 = types.KeyboardButton("Главное меню Бота")
    markup.row(btn1, btn2, btn3)
    markup.row(btn4)
    markup.row(btn5, btn6, btn7)
    markup.row(btn8, btn9,  btn10)
    markup.row(btn11)
    bot.send_message(message.from_user.id, 'Информация для персонала', reply_markup=markup)

def job_descrition(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Администратор")
    btn2 = types.KeyboardButton("Оператор")
    btn3 = types.KeyboardButton("Бармен")
    btn4 = types.KeyboardButton("Старший Бармен")
    btn5 = types.KeyboardButton("Официант")
    btn7 = types.KeyboardButton("Главное меню Бота")
    markup.row(btn1, btn2, btn3)
    markup.row(btn4, btn5)
    markup.row(btn7)
    bot.send_message(message.from_user.id, 'Должностные инструкции', reply_markup=markup)





@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Акции":
        pr.promotions(message)
    elif message.text == "Скидки":
        d.discount(message)
    elif message.text == "Сертификат, Купон, Розыгрыш, Промокод, Комбо":
        cpdc.coupon_promocode_draw_certificate(message)
    elif message.text == "Меню":
        menu(message)
    elif message.text == "Главное меню Бота":
        start(message)
    elif message.text == "Информация для персонала":
        info_for_staff(message)
    elif message.text == 'Должностные обязанности':
        job_descrition(message)
    elif message.text == 'Администратор':
        j.admin(message)
    elif message.text == 'Оператор':
        j.operator(message)
    elif message.text == 'Бармен':
        j.barmen(message)
    elif message.text == 'Старший Бармен':
        j.main_barmen(message)
    elif message.text == 'Официант':
        j.oficiant(message)
    else:
        bot.send_message(message.from_user.id, 'Я не знаю как реагировать на это. Смогу ответить когда мне дадут больше информации')








bot.polling(none_stop=True, interval=1)
  #for commit
