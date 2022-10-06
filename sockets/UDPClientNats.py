from socket import *

def send_nats(clientSocket, n, serverName, serverPort):
    for i in range(n):
        message = str(i) + ';'
        clientSocket.sendto(message.encode(), (serverName, serverPort))

if __name__ == '__main__':
    serverName = ''
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    n = 10
    send_nats(clientSocket, n, serverName, serverPort)
    clientSocket.close()
