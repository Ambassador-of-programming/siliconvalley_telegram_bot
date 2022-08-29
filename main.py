
from telebot import types
from random import randint

class Bot:
    def button(self, titles: str) -> object:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.max_row_keys = 3
        markup.row(*titles, '|||')
        return markup

    def random_menu(self):
        if randint(0,100) < 25:
            return ['◖Темы', '● Функции', 'Ссылки◗', '▸ Что за бот?']
        else: 
            return ['◖Темы', '● Функции', 'Ссылки◗']
    
    def menu(self):
        return self.button(self.random_menu())

# while True:
#     if randint(0,100) < 25:
#         print (['◖Темы', '● Функции', 'Ссылки◗', '▸ Что за бот?'])
#     else: 
#         print (['◖Темы', '● Функции', 'Ссылки◗'])
