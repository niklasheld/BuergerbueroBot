import telegram


class TelegramBot:

    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.bot = telegram.Bot(token=self.token)

    def send_message(self, message: str) -> None:
        self.bot.send_message(text=message, chat_id=self.chat_id)