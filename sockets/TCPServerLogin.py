from socket import *
import threading

def handle_conn(conn, Login, Password):
    c_addr = str(clientAddress)
    print('Connected with ' + c_addr)
    message = ''
    while True:
        acc = conn.recv(2048)
        message += acc.decode()
        if message.find(';') >= 0:
            break
    l = message.find('\n')
    login = message[0:l]
    p = message[l+1:].find(';')
    password = message[l+1:][:p]
    if login == Login and password == Password:
        print('Accepting:', login, 'with', password)
        conn.send("Ok!".encode())
    else:
        print('Blocking:', login, 'with', password)
        conn.send("Error!".encode())
    conn.close()

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('The server is ready to receive on port ' + str(serverPort))
    Login = 'root'
    Password = 'sudo'
    while True:
        (conn, clientAddress) = serverSocket.accept()
        t = threading.Thread(
                target=handle_conn,
                args=(conn, Login, Password))
        t.start()
