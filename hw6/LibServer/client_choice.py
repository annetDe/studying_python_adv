from library import Library
from msgutils import send_msg, recv_msg
import socket


def choice_msg() -> str:
    """Function with start message (with options)"""
    return 'How can I help you?\n'\
           '1 show all books in the library\n'\
           '2 show available books in the library\n'\
           '3 show unavailable books in the library\n'\
           '4 show all readers in the library\n'\
           '5 add book to the library\n'\
           '6 remove book from the library\n'\
           '7 give the book\n'\
           '8 return the book\n'\
           '9 add reader to the library\n'\
           '10 remove reader from the library\n'\
           '0 exit\n'\
           'make your choice: '


def choice_check(_choice: str) -> bool:
    """Function to check the response from the client"""
    if not _choice.isnumeric() or int(_choice) not in range(11):
        return False
    else:
        return True


def input_int(msg: str, conn: socket):
    send_msg(msg.encode(), conn)

    while True:
        answer = recv_msg(conn)
        if not answer:
            return False
        answer = answer.decode()
        if answer.isnumeric():
            return int(answer)
        else:
            error_msg = '\nInvalid input.\n' + msg
            send_msg(error_msg.encode(), conn)


def input_str(msg: str, conn: socket):
    send_msg(msg.encode(), conn)
    answer = recv_msg(conn)
    if not answer:
        return False
    return answer.decode()


def main_menu(conn: socket, lib: Library, choice: int):
    """Function for main menu actions accordingly to client choice
    Args:
        conn (socket): client's connection
        lib (Library): Library instance
        choice (int): client's choice
    """
    _choice = choice
    # 1 show all books in the library
    if _choice == 1:
        # генерирую строку книг
        books_str = '\n'.join([str(book) for book in lib.get_books()])
        if not books_str:
            books_str = 'There are no books in library.'
        # формирую сообщение на отправку
        msg = books_str+'\n\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 2 show available books in the library
    elif _choice == 2:
        # генерирую строку книг
        books_str = '\n'.join([str(book) for book in lib.get_books_in()])
        if not books_str:
            books_str = 'There are no available books in library.'
        # формирую сообщение на отправку
        msg = books_str+'\n\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 3 show unavailable books in the library
    elif _choice == 3:
        # генерирую строку книг
        books_str = '\n'.join([str(book) for book in lib.get_books_out()])
        if not books_str:
            books_str = 'There are no unavailable books in library.'
        # формирую сообщение на отправку
        msg = books_str+'\n\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 4 show all readers in the library
    elif _choice == 4:
        # генерирую строку читателей
        readers_str = '\n'.join([str(reader) for reader in lib.get_readers()])
        if not readers_str:
            readers_str = 'There are no readers in library.'
        # формирую сообщение на отправку
        msg = readers_str+'\n\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 5 add book to the library
    elif _choice == 5:
        title = input_str('Enter the title of the book: ', conn)
        author = input_str('Enter the author of the book: ', conn)
        year = input_int('Enter the year of publication of the book: ', conn)
        book_id = input_int('Enter the ISBN of the book: ', conn)
        res = lib.add_book(title, author, year, book_id)
        # формирую сообщение на отправку
        if res:
            msg = 'Book was successfully added\n'+choice_msg()
        else:
            msg = 'Invalid input\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 6 remove book from the library
    elif _choice == 6:
        book_id = input_int('Enter book id: ', conn)
        res = lib.del_book(book_id)
        # формирую сообщение на отправку
        if res:
            msg = 'Book was successfully delete.\n'+choice_msg()
        else:
            msg = 'Book is absent in the library.\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 7 give the book
    elif _choice == 7:
        book_id = input_int('Enter book id: ', conn)
        reader_id = input_int('Enter reader id: ', conn)
        res = lib.give_book(book_id, reader_id)
        # формирую сообщение на отправку
        if res:
            msg = 'Book was successfully given.\n'+choice_msg()
        else:
            msg = 'Book or reader is absent in the library.\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 8 return the book
    elif _choice == 8:
        book_id = input_int('Enter book id: ', conn)
        reader_id = input_int('Enter reader id: ', conn)
        res = lib.accept_book(book_id, reader_id)
        # формирую сообщение на отправку
        if res:
            msg = 'Book was successfully accepted.\n'+choice_msg()
        else:
            msg = 'Book or reader is absent in the library.\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 9 add reader to the library
    elif _choice == 9:
        name = input_str('Enter the name of the reader: ', conn)
        surname = input_str('Enter the surname of the reader: ', conn)
        year_birth = input_int('Enter the year of birth of the reader: ', conn)
        res = lib.add_reader(name, surname, year_birth)
        # формирую сообщение на отправку
        if res:
            msg = 'Reader was successfully added.\n'+choice_msg()
        else:
            msg = 'Invalid input\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 10 remove reader from the library
    elif _choice == 10:
        reader_id = input_int('Enter reader id: ', conn)
        res = lib.del_reader(reader_id)
        # формирую сообщение на отправку
        if res:
            msg = 'Reader was successfully delete.\n'+choice_msg()
        else:
            msg = 'Reader is absent in the library.\n'+choice_msg()
        # отправляю сообщение в байтах
        send_msg(msg.encode(), conn)
    # 0 exit
    elif _choice == 0:
        send_msg('Bye!'.encode(), conn)
