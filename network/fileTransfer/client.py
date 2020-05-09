import socket
import sys

# server ip & port
server_ip = '192.168.0.4'
server_port = 9999

# ready for client socket
client = socket.socket()

# connecting to server
client.connect((server_ip, server_port))
f = open('/Users/lhs/Desktop/asdf.png', 'rb')
l = f.read(1024)
while (l):
    client.send(l)
    l = f.read(1024)

client.close()