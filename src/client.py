import requests
import socket
import os
import webbrowser
import sys

LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 12346
if len(sys.argv) == 2:
    HOST, PORT = sys.argv[-1].split(':')
    PORT = int(PORT)
print(sys.argv)


def request(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        s.sendall(data)
        with open('index.html', 'w', encoding="ISO-8859-1") as f:
            while True:
                recv = s.recv(1024)
                print(recv)
                if not recv or recv == b"":
                    break
                f.write(recv.decode("ISO-8859-1"))

        webbrowser.open('file://' + os.getcwd() + '/index.html', new=2)


request(b"Hello World!")
