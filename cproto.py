import socket

s = socket.socket()

name = input('Your name:')
host_ip = input('host ip: ')

port = 8080

s.connect((host_ip, port))

s_name = s.recv(1024)
s_name = s_name.decode()
print(f'{s_name} joined\npress q to leave')
s.send(name.encode())

while True:
    message = s.recv(1024)
    message = message.decode()
    print(f'{s_name}: {message}')
    message = input(f'{name}: ')
    if message == 'q':
        message = f'{name} left'
        s.send(message.encode())
        break
    s.send(message.encode())
    