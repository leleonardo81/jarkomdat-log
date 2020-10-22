from socket import *
import random
import string

serverPort = 12000

serverSocket = socket(AF_INET,SOCK_STREAM)

serverSocket.bind(('localhost',serverPort))

serverSocket.listen(1)

session_store = {}

print('The server is ready...')

def login(command):
  name = command[1]
  id_session = ''.join(random.choices(string.ascii_letters + string.digits, k=5))
  session_store[id_session] = name
  return id_session

def process_message(command):
  id_session = command[1]
  message = " ".join(command[2:])
  client_name  = session_store.get(id_session)
  if client_name:
    return "ANSWER {} {}".format(client_name, message)
  return "ANSWER You are not logged in"
  

while(True):
  connectionSocket, addr = serverSocket.accept()
  print("There is new Connection")
  request = connectionSocket.recv(1024)
  command = request.decode().split()
  print("Receive a request -- ", command)

  if command[0].upper() == "LOGIN" and len(command) > 1:
    session_id = login(command)
    connectionSocket.send("NEW_SESSION {}".format(session_id).encode())
  elif command[0].upper() == "MSG" and len(command) > 2:
    connectionSocket.send(process_message(command).encode())
  else:
    connectionSocket.send("Wrong Command !".encode())

  print("")