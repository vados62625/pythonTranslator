from aiogram import Bot, Dispatcher, executor
import handlers

API_TOKEN = open('token.txt').read()
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.register_message_handler(handlers.start, commands=["start"])
dp.register_message_handler(handlers.setToLang, commands=["settolanguage"])
dp.register_message_handler(handlers.setFromLang, commands=["setfromlanguage"])
dp.register_message_handler(handlers.showSettings, commands=["showsettings"])
dp.register_message_handler(handlers.echo)
dp.register_callback_query_handler(handlers.changeToLang, lambda c: c.data and c.data.startswith('changeToLang'))
dp.register_callback_query_handler(handlers.changeFromLang, lambda c: c.data and c.data.startswith('changeFromLang'))

if __name__ == '__main__':

    executor.start_polling(dp, skip_updates=True)
