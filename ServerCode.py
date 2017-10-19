
import socket
import time
from socket import *
#from socket import socket, bind, listen, recv, send

HOST = '' #'127.0.1.1'  #localhost loopback
PORT = 8000

print ('Server is now live')
print ('HOST NAME : ', HOST)
print ('PORT : ', PORT)

s=socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn, addr = s.accept()

print ('Connected by : ', addr)

while True:
  data = conn.recv()
  print ("Received", repr(data))
  if not data: break
  reply = raw_input("Reply : ")
  conn.sendall(reply)

conn.close()
