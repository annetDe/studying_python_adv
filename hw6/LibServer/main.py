from client_choice import choice_msg, choice_check, main_menu
from msgutils import send_msg, recv_msg
from library import Library
import socket


lib = Library()
lib.load_books_from_txt_file('books.txt', sep='$!$')
lib.load_readers_from_txt_file('readers.txt')

with socket.socket() as sock:
    sock.bind(('', 1408))
    sock.listen(5)
    conn, _ = sock.accept()

    with conn:
        # отправить клиенту стартовое сообщение с выбором
        send_msg(choice_msg().encode('utf-8'), conn)
        while True:
            # получить ответ от клиента
            choice = recv_msg(conn).decode('utf-8')
            # если ответ клиента не проходит проверку
            if not choice_check(choice):
                send_msg(('\nInvalid choice.\n\n'+choice_msg()).encode('utf-8'), conn)
            #
            elif choice == '0':
                main_menu(conn, lib, int(choice))
                break
            else:
                main_menu(conn, lib, int(choice))
