from socket import *

def many_messages(clientSocket):
    message = input('~~> ')
    if message != '':
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifedMessage.decode())
        return False
    return True

def one_big_message(clientSocket):
    message = input(' -> ')
    m = None
    while m != '':
        m = input(' |> ')
        if m != '':
            message += '\n' + m
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifedMessage.decode())
    return True

def many_big_messages(clientSocket):
    message = input(' ~> ')
    m = None
    while m != '':
        m = input(' ~. ')
        if m != '':
            message += '\n' + m
    if message != '':
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        modifedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifedMessage.decode())
        return False
    return True

if __name__ == '__main__':
    serverName = ''
    serverPort = 12000
    clientSocket = socket(AF_INET, SOCK_DGRAM)

    # Para mim o enunciado não ficou claro,
    # deveria mandar várias mensagens ou
    # uma mensagem com '\n' no meio do caminho?
    # 0: várias mensagens de uma linha
    # 1: uma mensagem com '\n' no meio
    # 2: mistura, '\n\n' envia uma mensagem
    mode = 2
    exit = False
    while not exit:
        if mode == 0:
            exit = many_messages(clientSocket)
        elif mode == 1:
            exit = one_big_message(clientSocket)
        elif mode == 2:
            exit = many_big_messages(clientSocket)
        else:
            assert False, 'unhandled case for "mode": ' + str(mode)
    clientSocket.close()
