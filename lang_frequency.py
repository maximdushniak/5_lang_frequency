import re


def load_data(filepath):
    with open(filepath) as myfile:
        return myfile.read()


def get_most_frequent_words(text):
    mylist = re.sub('\W', ' ', text.lower()).split()

    newlist = list(set(mylist)) # удалим повторяющиеся элементы

    newlist.sort(key=lambda x: mylist.count(x), reverse=True)

    return newlist[0:9]


if __name__ == '__main__':
    filepath = input(u'Имя файла [data.txt]: ')
    if not filepath:
        filepath = 'data.txt'
    text = load_data(filepath)
    print(get_most_frequent_words(text))
