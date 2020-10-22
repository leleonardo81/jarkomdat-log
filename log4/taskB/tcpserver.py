from socket import *

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))

serverSocket.listen(1)

print('The server is ready to receive')

while(True):
  connectionSocket, addr = serverSocket.accept()
  sentence = connectionSocket.recv(1024)
  capitalizedSentence = sentence.upper()
  print('Message from client',sentence)
  print('Message answer for client',capitalizedSentence)
  connectionSocket.send(capitalizedSentence)
  connectionSocket.close()