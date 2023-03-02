import socket
import asyncio
import requests
import re
import random

HOST = "192.168.201.162"
PORT = random.randrange(20000, 30000)
print(PORT)

async def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connected to {addr}")
                data = conn.recv(1024)
                if not data:
                    break
                data = requests.get(data.decode("UTF-8")).content
                conn.sendall(data)

asyncio.run(server())
