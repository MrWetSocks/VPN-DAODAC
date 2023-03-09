#!/usr/bin/env python3
import requests
import socket
import os
import webbrowser
import sys

LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 12346
if len(sys.argv) == 3:
    HOST, PORT = sys.argv[-2].split(':')
    PORT = int(PORT)
    TERM = sys.argv[-1]
else:
    print("usage: client.py ip:port website")
print(sys.argv)


def request(data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        s.sendall(bytes(TERM, encoding="utf-8"))
        with open('index.html', 'w', encoding="utf-8") as f:
            while True:
                recv = s.recv(1024)
                if not recv or recv == b"":
                    break
                f.write(recv.decode(encoding="utf-8"))

        webbrowser.open('file://' + os.getcwd() + '/index.html', new=2)


request(b"Hello World!")
