from socket import *

def send_nats(clientSocket, n):
    for i in range(n):
        message = str(i) + ';'
        clientSocket.send(message.encode())

if __name__ == '__main__':
    serverName = ''
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, serverPort))
    n = 10
    send_nats(clientSocket, n)
    clientSocket.close()
