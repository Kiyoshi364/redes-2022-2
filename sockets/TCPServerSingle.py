from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen()
print('The server is ready to receive on port ' + str(serverPort))
persist = True
while True:
    (conn, clientAddress) = serverSocket.accept()
    print('Connected with ' + str(clientAddress))
    message = None
    while message != '':
        message = conn.recv(2048)
        if not message:
            break
        modifiedMessage = message.decode().upper()
        conn.send(modifiedMessage.encode())
        if not persist:
            print('Dropping')
            conn.close()
            break
    if persist:
        print('Disconnected')
        conn.close()
