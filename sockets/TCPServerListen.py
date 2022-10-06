from socket import *
import threading

def handle_conn(conn):
    c_addr = str(clientAddress)
    print('Connected with ' + c_addr)
    message = None
    while message != '':
        message = conn.recv(2048)
        if not message:
            break
        print(c_addr + ":", message.decode())
    conn.close()

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    serverSocket.listen()
    print('The server is ready to receive on port ' + str(serverPort))
    while True:
        (conn, clientAddress) = serverSocket.accept()
        t = threading.Thread(
                target=handle_conn,
                args=(conn,))
        t.start()
