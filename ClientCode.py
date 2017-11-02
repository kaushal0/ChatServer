## Client Code for Multiple Client Chat Server

import socket

def join():
	chatroom = input('Enter Chatroom Name to Enter : ')
	Cname = input('\nEnter Client Name : ')

	conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
	conn_msg += "CLIENT IP: \n".encode('utf-8')
	conn_msg += "PORT: \n".encode('utf-8')
	conn_msg += "CLIENT_NAME:".encode('utf-8') + Cname.encode('utf-8') + "\n".encode('utf-8')

s.send(conn_msg)



# creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = input('Enter the Hostname : ')
port = input('Port') 

# connection to hostname on the port.
s.connect((host, port))

Cname = input('Give Client Name')
join()
jID=0
data = s.recv(1024)
print(data.decode(encoding='utf-8'))
p = data.find(b'JOINED')
if p==0:
	jID_start = data.find('JOIN_ID'.encode('utf-8'))+9
	jID_end = data.find('\n'.encode('utf-8'),jID_start)-1
	jID = str(data[jID_start:jID_end])

serverThread = Client(s)
serverThread.start()


while(1):
	print('Enter Option to choose:')
	print('1. Join')
	print('2. Chat')
	print('3. Leave')
	print('4. Disconnect')
	task = input('?')
	if task == '1':
		join()
	elif task == '2':
		chat()
	elif task == '3':
		leave()
	elif task == '4':
		discon()
	elif task == '5':
		print('Error')
