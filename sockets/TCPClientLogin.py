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
    login = input('login: ')
    password = input('password: ')
    message = login + '\n' + password + ';'
    clientSocket.send(message.encode())
    answer = clientSocket.recv(2048)
    print(answer.decode())
    clientSocket.close()
