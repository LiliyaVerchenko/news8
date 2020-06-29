import json
from pprint import pprint
def read_news(file):
    with open ('newsafr.json', encoding='utf-8') as f:
        json.data = json.load(f)
        news_list = json.data['rss']['channel']['items']
        list5 = []
        for new in news_list:
            list5.extend(new['description'].split(' '))
    return list5

def choose_words():
    words_dict = {}
    ld = read_news('newsafr.json')
    for word in ld:
        if len(word) > 6:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    return words_dict

def top_word():
    words_dict1 = sorted(choose_words().items(), key=lambda х: х[1], reverse=True)[:10]
    for i, word in enumerate(words_dict1, 1):
        print(f'{i} место: "{word[0]}" - встречается в тексте {word[1]} раз')
top_word()
