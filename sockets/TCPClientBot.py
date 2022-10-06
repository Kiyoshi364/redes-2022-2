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

    clientSocket.send(';'.encode())
    skip = False
    msg = ''
    while True:
        toprint = ''
        sc = msg.find(';')
        d = msg.find('$')
        while sc == -1 and d == -1:
            msg += clientSocket.recv(2048).decode()
            sc = msg.find(';')
            d = msg.find('$')
        if sc != -1 and d == -1:
            toprint = msg[:sc]
            msg = msg[sc+1:]
            skip = False
        elif sc == -1 and d != -1:
            toprint = msg[:d]
            msg = msg[d+1:]
            if skip and toprint == '':
                if msg != '':
                    print('[WARNING]: ignoring trailing:', msg)
                break
            skip = True
        else:
            assert False, 'unreachable'
        print(toprint)
        if not skip:
            response = input('> ') + ';'
            clientSocket.send(response.encode())
    clientSocket.close()
