import socket

ip = '192.168.0.4'
port = 9999

server = socket.socket()
server.bind((ip, port))
server.listen(5)

