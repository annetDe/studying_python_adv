from annet_library.utils.book import Book
from annet_library.utils.reader import Reader
from annet_library.library import Library

book_1 = Book(1, 'Harry Potter and the Philosopher\'s Stone', 'J. K. Rowling', 1997)
book_2 = Book(2, 'Brave New World', 'Aldous Huxley', 1932)

reader_1 = Reader(1, 'John', 'Doe', 1985)
reader_2 = Reader(2, 'Jane', 'Doe', 1988)

library = Library()

# print(book_1)
# print(reader_1)

library.add_book(book_1)
library.add_book(book_2)
library.add_reader(reader_1)
library.add_reader(reader_2)

# library.del_book(1)
# library.del_reader(1)

library.print_books()
library.print_books_in()
library.print_books_out()

library.give_book(1, 1)
# print(book_1.get_reader_id())
# print(reader_1.get_books_id_lst())
library.accept_book(1, 1)
# print(book_1.get_reader_id())
# print(reader_1.get_books_id_lst())

# library.print_books()
# library.books_sort_title()
# library.print_books()
# library.books_sort_author()
library.books_sort_year()
library.print_books()
