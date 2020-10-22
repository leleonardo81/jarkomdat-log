from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('localhost', serverPort))

print ('The server is ready to receive')

while 1:
  message, clientAddress = serverSocket.recvfrom(2048)
  modifiedMessage = message.upper()
  print('Message from client',message)
  print('Message answer for client',modifiedMessage)
  serverSocket.sendto(modifiedMessage, clientAddress)