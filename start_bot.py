import telebot 
from config import TOKEN
from main import Bot
from random import randint

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    c = Bot()
    a = "Добро пожаловать {0.first_name}!!!\nЯ бот {1.first_name} созданный помогать людям 🧑🏼‍🏫\nПриступим к изучению Python".format(message.from_user, bot.get_me())
    bot.send_message(message.chat.id, a,reply_markup=c.menu())

    stiker = randint(1,6)
    stk_name = f'topics_stiker/{stiker}.tgs'     
    with open(stk_name, 'rb') as file:
        bot.send_sticker(message.chat.id, file)