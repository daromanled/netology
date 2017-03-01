import codecs
import json
def ten_words_from_news(country_news):
    Words = {}
    with codecs.open(country_news, encoding="utf-8") as news:
        for news in json.load(news)['rss']['channel']['item']:
           for word in news['description'].split():
               f = True
               for letter in word:
                   if letter not in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm':
                       f = False
               if f == True:
                    if word in Words.keys():
                        Words[word] += 1
                    else:
                        Words[word] = 1

    Words = sorted(Words.items(), key=lambda x:x[1], reverse = True)
    for top_word in Words[:11]:
        print(top_word[0])

country = input('Введите страну, топ слов из новостей которой вам нужен:')
if country == 'France' or country == 'Франция':
    ten_words_from_news('newsfr.json')
elif country == 'Cypr' or country == 'Кипр':
    ten_words_from_news('newscy.json')
elif country == 'Italy' or country == 'Италия':
    ten_words_from_news('newsit.json')
elif country == 'Africa' or country == 'Африка':
    ten_words_from_news('newsafr.json')
else:
    print('Sorry, we have not got any information about this country')
