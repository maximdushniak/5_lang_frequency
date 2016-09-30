import re


def load_data(filepath):
    with open(filepath) as myfile:
        return myfile.read()


def get_most_frequent_words(text):
    mylist = re.sub('\W', ' ', text).split()
    max_count = 0
    max_cntword = ''
    for i in mylist:
        count = mylist.count(i)
        if count>=max_count:
            max_count = count
            max_cntword = i
    return max_cntword


if __name__ == '__main__':
    filepath = input(u'Имя файла [data.txt]: ')
    if not filepath:
        filepath = 'data.txt'
    text = load_data(filepath)
    print(get_most_frequent_words(text))

