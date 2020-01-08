import socket

# open the server socket
server = socket.socket()
server.bind(('192.168.0.4', 9999))
server.listen(1)

# accept of client connection
client, addr = server.accept()
print('client is connected')

# receive to message
msg = client.recv(1024)
print('message has been received')
print(msg)

# send to message
client.send(b'welcome to server')
print('message has been sent')

client.close()
server.close()
