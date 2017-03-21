# coding=utf-8

from dictwrapper import DictWrapper


if __name__ == "__main__":

    book_list = [
        {'name': 'Guide to python',
         'author': {'name': 'Hugh', 'gender': 'male'},
         'pages': 219},

        {'name': 'The Three Kindoms',
         'author': {'name': 'Luo GuanZhong', 'gender': 'male'},
         'pages': 133}
    ]

    books = DictWrapper.load_dict(book_list)

    for book in books:
        print u"《%s》- %s" % (book.name, book.author.name)
