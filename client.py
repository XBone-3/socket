import socket, sys
import random
from threading import Thread
from tkinter.ttk import Separator
from colorama import Fore, init, Back
from datetime import datetime

init()
colors = [
    Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX, 
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX, 
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX, 
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

color = random.choice(colors)

s_host = "127.0.0.1"
port = 8080
Separator_token = "<SEP>"
name = input("Your name: ")
s = socket.socket()
# print(f'{name} is trying to connect')
s.connect((s_host, port))
print(f'{name} is connected')

def listen_for_messages():
    while True:
        msg = s.recv(1024).decode()
        print(msg)

t = Thread(target=listen_for_messages, daemon=True)
t.start()

while True:
    message = input()
    datenow = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{color} [{datenow}] {name}{Separator_token} {message}{Fore.RESET}"
    if message == "exit":
        message = f'{name} left the chat'
        s.send(message.encode())
        sys.exit()
    s.send(message.encode())
s.close()