from socket import *

serverName = 'localhost'

serverPort = 12000



print('Client app started...')

while True:
  command = input('Your command: ')
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName,serverPort))
  clientSocket.send(command.encode())

  response = clientSocket.recv(1024)

  print('>>>', response.decode())
  print("")
  clientSocket.close()