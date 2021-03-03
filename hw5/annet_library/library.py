class Library:
    def __init__(self):
        self.books_lst = []
        self.readers_lst = []

    def add_book(self, book):  # добавить книгу как объект
        self.books_lst.append(book)

    def del_book(self, book_id):  # удалить книгу по id
        for i in self.books_lst:
            if i.book_id == book_id:
                self.books_lst.remove(i)
                print(f'Book with id {book_id} was successfully delete.')
                break
        else:
            print(f'Book with id {book_id} is absent in the library.')

    def check_book(self, book_id):  # проверка существует ли книга в библиотеке
        for i in self.books_lst:
            if i.book_id == book_id:
                return True
        else:
            return False

    def add_reader(self, reader):  # добавить читателя как объект
        self.readers_lst.append(reader)

    def del_reader(self, reader_id):  # удалить читателя по id
        for i in self.readers_lst:
            if i.reader_id == reader_id:
                self.readers_lst.remove(i)
                print(f'Reader with id {reader_id} was successfully delete.')
                break
        else:
            print(f'Reader with id {reader_id} is absent in the library.')

    def check_reader(self, reader_id):  # проверка существует ли читатель в библиотеке
        for i in self.readers_lst:
            if i.reader_id == reader_id:
                return True
        else:
            return False

    def give_book(self, book_id, reader_id):  # отдать книгу читателю
        if self.check_book(book_id) and self.check_reader(reader_id):
            for i in self.books_lst:
                if i.book_id == book_id:
                    i.reader_id = reader_id
                    break
            for i in self.readers_lst:
                if i.reader_id == reader_id:
                    i.books_id_lst.append(book_id)
                    break
            print('Book was successfully given.')
        else:
            print(f'Book with id {book_id} or reader with id {reader_id} is absent in the library.')

    def accept_book(self, book_id, reader_id):  # принять книгу от читателя
        if self.check_book(book_id) and self.check_reader(reader_id):
            for i in self.books_lst:
                if i.book_id == book_id:
                    i.reader_id = None
                    break
            for i in self.readers_lst:
                if i.reader_id == reader_id:
                    i.books_id_lst.remove(book_id)
                    break
            print('Book was successfully accepted.')
        else:
            print(f'Book with id {book_id} or reader with id {reader_id} is absent in the library.')

    def print_books(self):  # вывести список всех книг
        print('All books:')
        for i in self.books_lst:
            print(i)

    def print_books_in(self):  # вывести список книг в наличии в библиотеке
        print('Available books:')
        for i in self.books_lst:
            if not i.reader_id:
                print(i)

    def print_books_out(self):  # вывести списк книг, которые не в наличии
        print('Unavailable books:')
        for i in self.books_lst:
            if i.reader_id:
                print(i)

    def books_sort_title(self):  # отсортировать список книг по названию
        self.books_lst.sort(key=lambda book: book.title)  # меняет изначальный список
        # print(sorted(self.books_lst, key=lambda book: book.title))  # не меняет изначальный список

    def books_sort_author(self):  # отсортировать список книг по автору
        self.books_lst.sort(key=lambda book: book.author)  # меняет изначальный список
        # print(sorted(self.books_lst, key=lambda book: book.author))  # не меняет изначальный список

    def books_sort_year(self):  # отсортировать список книг по году издания
        self.books_lst.sort(key=lambda book: book.year)  # меняет изначальный список
        # print(sorted(self.books_lst, key=lambda book: book.year))  # не меняет изначальный список
