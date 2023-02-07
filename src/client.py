import requests
import socket
import os
import webbrowser
import sys

LOCAL_HOST = "127.0.0.1"
LOCAL_PORT = 12345
if len(sys.argv) == 2:
    HOST, PORT = sys.argv[-1].split(':')
    PORT = int(PORT)
print(sys.argv)
def receive_request():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((LOCAL_HOST, LOCAL_PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            with open('index.html', 'w') as f:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    f.write(data)

                # conn.sendall(data)
            webbrowser.open('file://' + os.getcwd() + '/index.html', new=2)

def send_request(dat):
    print('hej')
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"Connected to {HOST}:{PORT}")
        s.sendall(dat)
    
    return

send_request(b"lkajslkjflkj")
receive_request()