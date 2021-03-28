from socket import socket

default_header_size = 10
default_size_pack = 1024
encoding = 'utf-8'

def send_msg(msg: bytes,
             conn: socket,
             header_size: int = default_header_size) -> bool:
    # определяем размер сообщения, готовим заголовок
    size_msg = f'{len(msg):{header_size}}'

    # отправляем заголовок
    if conn.send(size_msg.encode(encoding)) != header_size:
        print('ERROR: can\'t send size message')
        return False

    # отправляем сообщение
    if conn.send(msg) != len(msg):
        print('ERROR: can\'t send message')
        return False

    return True

def recv_msg(conn: socket,
             header_size: int = default_header_size,
             size_pack: int = default_size_pack):
    data = conn.recv(header_size)
    if not data or len(data) != header_size:
        print('ERROR: can\'t read size message')
        return False

    size_msg = int(data.decode(encoding))
    msg = b''
    while True:
        if size_msg <= size_pack:
            pack = conn.recv(size_msg)
            if not pack:
                return False

            msg += pack
            break
        pack = conn.recv(size_pack)
        if not pack:
            return False

        size_msg -= size_pack
        msg += pack

    return msg
