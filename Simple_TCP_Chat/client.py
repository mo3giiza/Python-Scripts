import socket

host = '127.0.0.1'
port = 9001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

done = False

while not done:
	client.send(input("Enter Message: ").encode('utf-8'))
	message = client.recv(1024).decode('utf-8')
	if message == 'exit':
		done = True
	else:
		print(message)

client.close()