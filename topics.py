from main import Bot

class Message:
    def __init__(self, bot, message) -> None:
        self.bot = bot 
        self.chat = message.chat.id
        self.func = Bot()

    def tems(self):
        markup = self.func.button(['Скачать Python', 'Установка редактора исходного кода', 'Условия', 'Типы данных', 'List&Tuple','Set&Dict'])           
        self.bot.send_message(self.chat, 'Темы', reply_markup=markup)
