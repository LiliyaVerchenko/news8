from pprint import pprint
import xml.etree.ElementTree as ET

def read_news(file):
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse('newsafr.xml', parser)
    root = tree.getroot()
    # print(root.tag)
    # print(root.text)
    # print(root.attrib)

    news_list = root.findall('channel/item/description')
    list5 = []
    for new in news_list:
        list5.extend(new.text.split(' '))
    return list5

def choose_words():
    words_dict = {}
    list5 = read_news('newsafr.json')
    for word in list5:
        if len(word) > 6:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
    return words_dict

def top_word():
    words_dict1 = sorted(choose_words().items(), key=lambda х: х[1], reverse=True)[:10]
    for i, word in enumerate(words_dict1, 1):
        print(f'{i} место: слово "{word[0]}" - встречается в тексте {word[1]} раз')

top_word()









