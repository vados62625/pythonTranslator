from aiogram import types
from translate import Translator


async def start(message: types.Message):
    
    await message.answer("Привет!\nНапиши мне что-нибудь, а я попробую перевести!")


async def echo(message: types.Message):
    
    with open("chathistory.txt", "a") as file:
        file.write('\n' + message.from_user.username + ' написал: ' + message.text)
    translator = Translator(from_lang='russian', to_lang='english')
    translation = translator.translate(message.text)
    await message.answer(translation)
