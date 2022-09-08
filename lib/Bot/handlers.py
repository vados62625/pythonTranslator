from aiogram import types
from googletrans import Translator
from datetime import datetime

translator = Translator()

async def start(message: types.Message):
    
    await message.answer("Привет!\nНапиши мне что-нибудь, а я попробую перевести!")


async def echo(message: types.Message):

    #translator = Translator(from_lang='russian', to_lang='english')    
    translation = translator.translate(message.text)
    await message.answer(translation.text)
    with open("chathistory.txt", "a") as file:
        file.write('\n' + datetime.now().strftime("%d/%m/%Y %H:%M:%S") + '\t' + message.from_user.username + ' написал: ' + message.text + '\tБот ответил: ' + translation.text)
