# import socket library
import socket

# ip address for localhost and port number
host = '127.0.0.1'
port = 9001

#########################################################
# 1. create new socket that we got from socket library  #
# 2. socket.AF_INET to define that is internet socket   #
#    for internet communications for example Bluetooth, #
#    Infrared and .... etc.				#
# 3. socket.SOCK_STREAM define it's stream based socket #
#    and it's connection orinted using TCP Protocol     #
#########################################################
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# binding this socket into 
# localhost on port 9001 and listening
server.bind((host, port))
server.listen()

# Accept incoming connections
# client that can used for communicating
# and his address 
client, addr = server.accept()

done = False

# Basic while loop for receiving anything
# from client and decode it using UTF-8
while not done:
	message = client.recv(1024).decode('utf-8')
	if message == 'exit':
		done = True
	else:
		print(message)

	client.send(input("Enter Message: ").encode('utf-8'))

# Closing the sockets
client.close()
server.close()
