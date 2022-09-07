from aiogram import Bot, Dispatcher, executor
import handlers


API_TOKEN = '5770068201:AAHVELfQ6f2DzYacmOMV1R3rBpBzDo6woCg'


# создаем экземпляры бота и диспетчера


bot = Bot(token=API_TOKEN)


dp = Dispatcher(bot)

# регистрируем функции

dp.register_message_handler(handlers.start, commands=["start"])

dp.register_message_handler(handlers.echo)

# запускаем программу


if __name__ == '__main__':


# указание skip_updates=True


# пропустит команды,


# которые отправили


# до старта бота

    executor.start_polling(dp, skip_updates=True)
