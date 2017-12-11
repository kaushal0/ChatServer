## Client Code for Multiple Client Chat Server

import socket
import sys
from threading import Thread

def join():
	chatroom = input('Enter Chatroom Name to Enter : ')

	conn_msg = "JOIN_CHATROOM:".encode('utf-8') + chatroom.encode('utf-8') + "\n".encode('utf-8')
	conn_msg += "CLIENT IP: \n".encode('utf-8')
	conn_msg += "PORT: \n".encode('utf-8')
	conn_msg += "CLIENT_NAME:".encode('utf-8') + Clname.encode('utf-8') + "\n".encode('utf-8')
	s.send(conn_msg)

def chat(socket):
	croom = input('Which room to send message? ')
	chat_message = input('Enter Message to send: ')
	msg = "CHAT: ".encode('utf-8') + croom.encode('utf-8') + "\n".encode('utf-8')
	msg += "JOIN_ID: ".encode('utf-8') + str(jID).encode('utf-8') + "\n".encode('utf-8')
	msg += "CLIENT_NAME: ".encode('utf-8') + Clname.encode('utf-8') + "\n".encode('utf-8')
	msg += "MESSAGE: ".encode('utf-8') + chat_message.encode('utf-8') + "\n\n".encode('utf-8')
	s.send(msg)

def disconnect():
 	msg = "DISCONNECT: \n".encode('utf-8')
 	msg += "PORT: \n".encode('utf-8')
 	msg += "CLIENT_NAME: ".encode('utf-8') + Clname.encode('utf-8') + "\n".encode('utf-8')
 	s.send(msg)

 	s.close()
 	os._exit(1)

def leave(socket):
	rTL = input('Room to Leave ')
	msg = "LEAVE_CHATROOM: ".encode('utf-8') + rTL.encode('utf-8') + "\n".encode('utf-8')
	msg += "JOIN_ID: ".encode('utf-8') + jID.encode('utf-8') + "\n".encode('utf-8')
	msg += "CLIENT_NAME: ".encode('utf-8') + Clname.encode('utf-8')
	socket.send(msg)


class client_thread(Thread):
	def __init__(self, socket):
		Thread.__init__(self)
		self.socket= socket

	def run(self):
		while True:
			data = self.socket.recv(1024)
			print("Client Message : ")
			print(data.decode(encoding='utf-8'))


# creating the socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = input('Enter the Hostname : ')
port = input('Port')

# connecting to host
s.connect((host, int(port)))

#Basic response test

Clname = input('Give Client Name')
join()
jID=0
data = s.recv(1024)
print(data.decode(encoding='utf-8'))
p = data.find(b'JOINED')
if p==0:
	jID_start = data.find('JOIN_ID'.encode('utf-8'))+9
	jID_end = data.find('\n'.encode('utf-8'),jID_start)-1
	jID = str(data[jID_start:jID_end])

cThread = client_thread(s)
cThread.start()

while(True):
	print('Enter Option to choose:')
	print('1. Join')
	print('2. Chat')
	print('3. Leave')
	print('4. Disconnect')
	task = input('')
	if task == '1':
		join()
	elif task == '2':
		print("Chat")
		chat(s)
	elif task == '3':
		leave()
	elif task == '4':
		disconnect()
	elif task == '5':
		print('Error. Please Enter Correct value')
