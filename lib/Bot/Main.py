from aiogram import Bot, Dispatcher, executor
import handlers

API_TOKEN = open('token.txt').read()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.echo)

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
