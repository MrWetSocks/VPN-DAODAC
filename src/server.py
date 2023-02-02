import socket

s = socket.socket()

port = 12345

s.bind(("", port))
s.listen(5)

while True:
    c, addr = s.accept()
    print(addr)
    c.send("Connected".encode())
    print(c.recv(1024).decode())
