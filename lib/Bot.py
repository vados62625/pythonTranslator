from telethon import TelegramClient,sync, events, types
from googletrans import Translator
class BotHandler:
    
    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        try:
            get_result = self.get_updates()
            if len(get_result) > 0:
                last_update = get_result[-1]
            else:
                last_update = get_result[len(get_result)]
            return last_update
        except IndexError:
          print('except')

def main(lastdate,lastid):
    translator_bot = BotHandler('5770068201:AAHVELfQ6f2DzYacmOMV1R3rBpBzDo6woCg')
    new_offset = None
    
    while True:
        translator_bot.get_updates(new_offset)
        last_update = your_bot.get_last_update()
        last_update_id = last_update['update_id']
        last_chat_text = last_update['message']['text']
        last_chat_id = last_update['message']['chat']['id']
        last_chat_name = last_update['message']['chat']['first_name']
        last_chat_date=last_update['message']['date']
        if (last_chat_date!=lastdate):
            lastdate=last_chat_date
            message(last_update,last_update_id,last_chat_text,last_chat_id,last_chat_name,last_chat_date)

def message(last_update,last_update_id,last_chat_text,last_chat_id,last_chat_name,last_chat_date):
    language = 'english'
    translator = Translator(from_lang='russian', to_lang=language)
    translation = translator.translate(last_chat_text)
    translator_bot.send_message(last_chat_id, translation)

