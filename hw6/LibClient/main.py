from msgutils import send_msg, recv_msg
import socket


with socket.socket() as sock:
    sock.connect(('localhost', 1408))

    while True:
        # получить сообщение
        rec_msg = recv_msg(sock).decode('utf-8')
        # если сообщение не пришло
        if not rec_msg:
            print('ERROR: can\'t receive message')
            exit(0)
        # если сообщение пришло 'Bye!'
        elif rec_msg == 'Bye!':
            print(rec_msg)
            exit(0)
        # отправить серверу свой выбор
        send_msg(input(rec_msg).encode('utf-8'), sock)
