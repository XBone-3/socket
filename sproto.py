import socket

s = socket.socket()
host = socket.gethostname()
ip = socket.gethostbyname(host)
name = input('Your name: ')
port = 8080
print(f'you are at {ip}:{port}')
s.bind((host, port))
print('listening...')
s.listen(4)
conn, addr = s.accept()
conn.send(name.encode())
c_name = conn.recv(1024)
c_name = c_name.decode()
print(f'{c_name} joined\nPress q to leave')

while True:
    message = input(f'{name}: ')
    if message == "q":
        message = f'{name} left'
        conn.send(message.encode())
        break
    conn.send(message.encode())
    message = conn.recv(1024)
    message = message.decode()
    print(f'{c_name}: {message}')

