from aiogram import types
import googletrans
from googletrans import Translator
from datetime import datetime
import collections.abc
import json

translator = Translator()
langSrc = 'auto'
langDest = 'en'
languages = googletrans.LANGUAGES
languages["auto"] = "автоматически"


async def start(message: types.Message):
    
    await message.answer("Привет!\nНапиши мне что-нибудь, а я попробую перевести!")
    usersData = ''
    with open("data.json", "r") as file:
        usersData = json.load(file)
        if not message.from_user.username in usersData:
            usersData[message.from_user.username] = {"toLang":langDest, "fromLang":langSrc}            
            with open("data.json", "w") as file:
                json.dump(usersData, file, ensure_ascii=False, indent=4)
    


async def echo(message: types.Message):
    
    langSrc = getLangFrom(message.from_user.username)
    langDest = getLangTo(message.from_user.username)
    
    answerMessage = translate(message.text, langSrc, langDest)

    await message.answer(answerMessage)
    
    with open("chathistory.txt", "a") as file:
        nl_char = '\n'
        tab_char = '\t'
        file.write(f'\n{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\t{message.from_user.username} написал: {message.text.replace(nl_char, tab_char)}\tБот ответил: {answerMessage.replace(nl_char, tab_char)}')

    
async def setFromLang(message: types.Message):
    
    inline_kb = types.InlineKeyboardMarkup()
    inline_btn_1 = types.InlineKeyboardButton('Определять автоматически', callback_data=f'changeFromLang=auto')
    inline_kb.add(inline_btn_1)
    for lang in languages:
        inline_btn_1 = types.InlineKeyboardButton(languages[lang], callback_data=f'changeFromLang={lang}')
        inline_kb.add(inline_btn_1)
    await message.answer('Выберите язык из списка:', reply_markup=inline_kb)


async def setToLang(message: types.Message):
    
    inline_kb = types.InlineKeyboardMarkup()
    for lang in languages:
        inline_btn_1 = types.InlineKeyboardButton(languages[lang], callback_data=f'changeToLang={lang}')
        inline_kb.add(inline_btn_1)
    await message.answer('Выберите язык из списка:', reply_markup=inline_kb)

    
async def changeFromLang(callback_query: types.CallbackQuery):
    
    langSrc = callback_query.data[15:]
    await callback_query.message.answer(f'Исходный язык изменен на: {languages[langSrc]}')
    with open("data.json", "r") as file:
        usersData = json.load(file)
        usersData[callback_query.from_user.username]["fromLang"] = langSrc
        with open("data.json", "w") as file:
            json.dump(usersData, file, ensure_ascii=False, indent=4)        
    await callback_query.answer()
    await callback_query.message.delete()


async def changeToLang(callback_query: types.CallbackQuery):
    
    langDest = callback_query.data[13:]
    await callback_query.message.answer(f'Язык перевода изменен на: {languages[langDest]}')
    with open("data.json", "r") as file:
        usersData = json.load(file)
        usersData[callback_query.from_user.username]["toLang"] = langDest
        with open("data.json", "w") as file:
            json.dump(usersData, file, ensure_ascii=False, indent=4)        
    await callback_query.answer()
    await callback_query.message.delete()


async def showSettings(message: types.Message):

    user = message.from_user.username
    langSrc = getLangFrom(user)
    if getLangFrom(user) == None:
        langSrc = "auto"
    await message.answer(f'Исходный язык: {languages[langSrc]}\nЯзык перевода: {languages[getLangTo(user)]}')
    

def translate(text, src=None, dest=None):

    translation = ''
    langSrc = ''

    if src == None:
        src = translator.detect(text).lang
    
    if dest == None:
        dest = 'en'    

    if not isinstance(src, str):
        for lang in src:
            langSrc = f'{languages[lang]} (определено автоматически)'
            translation += f'Перевод: {translator.translate(text, src=lang, dest=dest).text}\nИсходный язык: {langSrc}\nЯзык перевода: {languages[dest]}\n\n'
    else:
        langSrc = f'{languages[src]}'
        translation = f'Перевод: {translator.translate(text, src=src, dest=dest).text}\nИсходный язык: {languages[src]}\nЯзык перевода: {languages[dest]}\n\n'
    return translation


def getLangTo(user):
    
    with open("data.json", "r") as file:
        usersData = json.load(file)
        if user in usersData:
            return usersData[user]["toLang"]
        else: return None

        
def getLangFrom(user):
    
    with open("data.json", "r") as file:
        usersData = json.load(file)
        if user in usersData:
            if "fromLang" in usersData[user]:
                if not usersData[user]["fromLang"] == "auto":
                    return usersData[user]["fromLang"]
        else: return None
