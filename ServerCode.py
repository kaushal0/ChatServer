
import socket
import time
from socket import *
from threading import Thread
import random
#from socket import socket, bind, listen, recv, send

def check_msg(msg):
	if (msg.find('JOIN_CHATROOM'.encode('utf-8'))+1):
		return(1)
	elif (msg.find('LEAVE_CHATROOM'.encode('utf-8'))+1):
		return(2)
	elif (msg.find('DISCONNECT'.encode('utf-8'))+1):
		return(3)
	elif (msg.find('CHAT:'.encode('utf-8'))+1):
		return(4)
	else:
		return(5)
  

class client_threads(Thread):

	def __init__(self,ip,port,socket):
		Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.chatroom =[]
		self.socket = socket
		self.uid = random.randint(1000,2000)

	def run(self):
		while True:
			conn_msg = csock.recv(1024)
			cflag = check_msg(conn_msg)
#			print(conn_msg)
		  if cflag == 1 :                      #joining the room
#			elif cflag == 2 : leave()
#			elif cflag == 3 : discon(csock)      #yet to implement
#		  elif cflag == 4 : chat()
      else : pass		         			         #assigning error code for incorrect message
#			print(self.name)


s=socket(AF_INET, SOCK_STREAM)
HOST = '' #'127.0.1.1'  #localhost loopback
PORT = 8000

print ('Server is now live')
print ('HOST NAME : ', HOST)
print ('PORT : ', PORT)

s.bind((HOST, PORT))
thread_count = []

conn, addr = s.accept()

print ('Connected by : ', addr)

while True:
  s.listen(4)
  (csock,(ip,port)) = server.accept()

	print("Connected to ",port,ip)
	#monitoring connections

	clThread = client_threads(ip,port,csock)
	clThread.start()
	thread_count.append(clThread)
	print("Threads :")
	print(thread_count)

conn.close()
