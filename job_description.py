import telebot
from telebot import types
bot=telebot.TeleBot('5815341263:AAFMT3W01H6vO8-f9nvpxDtVKnSaB6eK2DE')

def admin(message):
    with open(' job_description\Администратор.txt', 'r', encoding='utf-8') as txt:
        n= txt.read()
        bot.send_message(message.from_user.id, n)
def main_barmen(message):
    with open(' job_description\Старший бармен.txt', 'r', encoding='utf-8') as txt:
        n= txt.read()
        bot.send_message(message.from_user.id, n)
def barmen(message):
    with open(' job_description\Бармен.txt', 'r', encoding='utf-8') as txt:
        n= txt.read()
        bot.send_message(message.from_user.id, n)
def operator(message):
    with open(' job_description\Оператор', 'r', encoding='utf-8') as txt:
        n= txt.read()
        bot.send_message(message.from_user.id, n)
def oficiant(message):
    with open(' job_description\Оффициант.txt', 'r', encoding='utf-8') as txt:
        n= txt.read()
        bot.send_message(message.from_user.id, n)