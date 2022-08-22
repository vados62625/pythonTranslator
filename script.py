from translate import Translator
from sys import argv
if len(argv) == 3:
    script, language, textToTranslate = argv
elif len(argv) == 2:
    script, textToTranslate = argv
    language = 'english'
else: print('Неправильный формат ввода')
translator = Translator(from_lang='russian', to_lang=language)
translation = translator.translate(textToTranslate)
print(translation)
