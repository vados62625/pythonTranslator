from aiogram import types


# функция, обрабатывающая команду /start

async def start(message: types.Message):

    await message.answer("Привет!\nНапиши мне что-нибудь!")


# функция, которая отвечает на сообщение

# текстом

async def echo(message: types.Message):

    await message.answer("Сам ты: " + message.text)
