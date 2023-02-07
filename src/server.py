import socket
import asyncio

HOST = "localhost"
PORT = 12346

async def loop():
    while True:
        with socket.socket() as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected to {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    if data == b"exit\n":
                        break

                    conn.sendall(b"Message recieved\n")
                    print(data.decode())

asyncio.run(loop())
