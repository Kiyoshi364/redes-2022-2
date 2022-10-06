from socket import *
serverName = ''
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifedMessage.decode())
clientSocket.close()
