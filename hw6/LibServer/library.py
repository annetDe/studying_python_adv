from book import Book
from reader import Reader
import os


class Library:
    def __init__(self,
                 books: list = None,
                 readers: list = None) -> None:
        self.__books_lst = books if books else []
        self.__readers_lst = readers if readers else []

    # LOADING BOOKS IN LIBRARY
    def load_books_from_txt_file(self,
                                 filename: str,
                                 sep: str = ',',
                                 encoding: str = 'utf-8') -> bool:
        # проверка существует ли такой файл
        if not os.path.exists(filename):
            print(f'ERROR: file \'{filename}\' not found.')
            return False
        # открыть файл и считать его
        with open(filename, encoding=encoding) as _f:
            # для каждой строки в файле
            for _line in _f:
                # удалить пробелы в начале и конце строки + разбить по sep в список
                _line_lst = _line.strip().split(sep)
                # добавить книгу в список книг
                self.__books_lst.append(Book(
                    _line_lst[0],  # title
                    _line_lst[1],  # author
                    int(_line_lst[2])  # year
                ))
        return True

    # LOADING READERS IN LIBRARY
    def load_readers_from_txt_file(self,
                                   filename: str,
                                   sep: str = ',',
                                   encoding: str = 'utf-8') -> bool:
        # проверка существует ли такой файл
        if not os.path.exists(filename):
            print(f'ERROR: file \'{filename}\' not found.')
            return False
        # открыть файл и считать его
        with open(filename, encoding=encoding) as _f:
            # для каждой строки в файле
            for _line in _f:
                # удалить пробелы в начале и конце строки + разбить по sep в список
                _line_lst = _line.strip().split(sep)
                # добавить книгу в список книг
                self.__readers_lst.append(Reader(
                    _line_lst[0],  # name
                    _line_lst[1],  # surname
                    int(_line_lst[2])  # year_birth
                ))
        return True

    # добавить книгу
    def add_book(self,
                 title: str,
                 author: str,
                 year: int,
                 id_: int = None) -> bool:
        books_id = [book.get_id() for book in self.__books_lst]
        if id_ in books_id:
            return False
        book = Book(title, author, year, id_)
        self.__books_lst.append(book)
        return True

    # удалить книгу по id
    def del_book(self, book_id: int) -> bool:
        for book in self.__books_lst:
            if book.get_id() == book_id:
                self.__books_lst.remove(book)
                return True
        else:
            return False

    # проверка существует ли книга в библиотеке
    def check_book(self, book_id: int) -> bool:
        for book in self.__books_lst:
            if book.get_id() == book_id:
                return True
        else:
            return False

    # добавить читателя
    def add_reader(self,
                   name: str,
                   surname: str,
                   year_birth: int,
                   id_: int = None) -> bool:
        readers_id = [reader.get_id() for reader in self.__readers_lst]
        if id_ in readers_id:
            return False
        reader = Reader(name, surname, year_birth, id_)
        self.__readers_lst.append(reader)
        return True

    # удалить читателя по id
    def del_reader(self, reader_id: int) -> bool:
        for reader in self.__readers_lst:
            if reader.get_id() == reader_id:
                self.__readers_lst.remove(reader)
                return True
        else:
            return False

    # проверка существует ли читатель в библиотеке
    def check_reader(self, reader_id: int) -> bool:
        for reader in self.__readers_lst:
            if reader.get_id() == reader_id:
                return True
        else:
            return False

    # отдать книгу читателю
    def give_book(self, book_id: int, reader_id: int) -> bool:
        if self.check_book(book_id) and self.check_reader(reader_id):
            for book in self.__books_lst:
                if book.get_id() == book_id:
                    book.set_reader_id(reader_id)
                    break
            for reader in self.__readers_lst:
                if reader.get_id() == reader_id:
                    reader.add_book_id(book_id)
                    break
            return True
        else:
            return False

    # принять книгу от читателя
    def accept_book(self, book_id: int, reader_id: int) -> bool:
        if self.check_book(book_id) and self.check_reader(reader_id):
            for book in self.__books_lst:
                if book.get_id() == book_id and book.get_reader_id() == reader_id:
                    book.set_reader_id(None)
                    break
                else:
                    return False
            for reader in self.__readers_lst:
                if reader.get_id() == reader_id and book_id in reader.get_books_id_lst():
                    reader.remove_book_id(book_id)
                    break
                else:
                    return False
            return True
        else:
            return False

    # вернуть список всех книг
    def get_books(self) -> list:
        return self.__books_lst

    # вернуть список книг в наличии в библиотеке
    def get_books_in(self) -> list:
        res_books = [i for i in self.__books_lst if not i.get_reader_id()]
        return res_books

    # вернуть списк книг, которые не в наличии
    def get_books_out(self) -> list:
        res_books = [i for i in self.__books_lst if i.get_reader_id()]
        return res_books

    # вернуть список всех читателей
    def get_readers(self) -> list:
        return self.__readers_lst

    # отсортировать список книг по названию
    def books_sort_title(self) -> None:
        self.__books_lst.sort(key=lambda book: book.title)  # меняет изначальный список
        # print(sorted(self.books_lst, key=lambda book: book.title))  # не меняет изначальный список

    # отсортировать список книг по автору
    def books_sort_author(self) -> None:
        self.__books_lst.sort(key=lambda book: book.author)  # меняет изначальный список
        # print(sorted(self.books_lst, key=lambda book: book.author))  # не меняет изначальный список

    # отсортировать список книг по году издания
    def books_sort_year(self) -> None:
        self.__books_lst.sort(key=lambda book: book.year)  # меняет изначальный список
        # print(sorted(self.books_lst, key=lambda book: book.year))  # не меняет изначальный список
