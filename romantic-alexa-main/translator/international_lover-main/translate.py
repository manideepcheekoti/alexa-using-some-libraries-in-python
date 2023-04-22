import googletrans

translator = googletrans.Translator()
translated  = translator.translate("I am a lovely romantic person.",dest='te')
print(translated)

# print(googletrans.LANGUAGES)
