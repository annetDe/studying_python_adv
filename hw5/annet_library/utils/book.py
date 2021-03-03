class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.reader_id = None

    def __repr__(self):
        return f'\tid:\t\t{self.book_id}\n\ttitle:\t{self.title}\n\tauthor:\t{self.author}\n\tyear:\t{self.year}\n'

    def get_reader_id(self):
        return self.reader_id
