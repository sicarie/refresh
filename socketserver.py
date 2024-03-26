import socket

# https://code.tutsplus.com/introduction-to-network-programming-in-python--cms-30459t
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = 'localhost'
port = 9090

sock.bind((host, port))
sock.listen(1)

print('waiting for a connection')
connection, client = sock.accept()
print(client, 'connected')
 
# Receive the data in small chunks and retransmit it 
#data = connection.recv(16)
data = connection.recv(64)
print('received "%s"' % data)
if data:
    connection.sendall(data)
else:
    print('no data from', client)

connection.close()
