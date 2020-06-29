
def read_news(file):
    import json
    from pprint import pprint
    with open ('newsafr.json', encoding='utf-8') as f:
        json.data = json.load(f)
        news_list = json.data['rss']['channel']['items']
        for new in news_list:
            list_1 = new['description'].strip().lower().split()
    return list_1

# read_news('newsafr.json')

def choose_words():
    words_dict = {}
    ld = read_news('newsafr.json')
    count = 0
    for word in ld:
        if len(word) > 6:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    return print(words_dict)
choose_words()

#return print(sorted(words_dict.items(), key=lambda х: х[1], reverse=True)[:10])

