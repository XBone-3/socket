import socket
from threading import Thread

from debugpy import listen

host = "0.0.0.0"
port = 8080
separator_token = '<SEP>'
client_sockets = set()
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host, port))
s.listen(5)

def listen_for_clients(cs):
    while True:
        try:
            msg = cs.recv(1024).decode()
        except Exception as e:
            print(f'error: {e}')
            client_sockets.remove(cs)
        else:
            msg = msg.replace(separator_token, ': ')
        for client in client_sockets:
            client.send(msg.encode())
    
while True:
    client_socket, address = s.accept()
    client_sockets.add(client_socket)
    t = Thread(target = listen_for_clients, args = (client_socket,), daemon=True)
    t.start()

for cs in client_sockets:
    cs.close()

s.close()