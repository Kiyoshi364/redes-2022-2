from socket import *
import threading

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print('The server is ready to receive on port ' + str(serverPort))
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        print(message.decode())
