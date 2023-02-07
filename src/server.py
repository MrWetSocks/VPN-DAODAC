import socket
import asyncio
import requests

HOST = "localhost"
PORT = 12345

async def loop():
    with socket.socket() as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected to {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data == b"exit\n":
                        break
                    conn.sendall(requests.get("https://google.com").content)
                    conn.sendall(b"Message recieved\n")
                    print(data.decode())

asyncio.run(loop())
