## Client Code for Multiple Client Chat Server

import socket

# creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = input('Enter the Hostname : ')
port = 8000
# connection to hostname on the port.
s.connect((host, port))

chatroom = input('Enter Chatroom Name to Enter : ')
Cname = input('\nEnter Client Name : ')

conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
conn_msg += "CLIENT IP: \n".encode('utf-8')
conn_msg += "PORT: \n".encode('utf-8')
conn_msg += "CLIENT_NAME:".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')

s.send(conn_msg)

while(1):
	message = s.recv(1024)
	print('Enter Option to choose:')
	print('1. Join')
	print('2. Chat')
	print('3. Leave')
	print('4. Disconnect')
	task = input('')
	if task == 1:
		join()
	elif task == 2:
		chat()
	elif task == 3:
		leave()
	elif task == 4:
		discon()
	elif task == 5:
		print('Error')
