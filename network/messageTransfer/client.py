import socket

# Server IP & port
ip = '192.168.0.4'
port = 9999

# ready for client socket
client = socket.socket()

# connecting to server
client.connect((ip, port))
print('Server is connected')

# send to message
print('input the Message')
client.send(b'Hello')

# receive to message
msg = client.recv(1024)
print('receive to message')
print(msg)

client.close()

