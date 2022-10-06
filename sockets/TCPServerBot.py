from socket import *
import threading

def advance(conn, str):
    i = str.find(';')
    while i == -1:
        str += conn.recv(2048).decode()
        i = str.find(';')
    tok = str[:i]
    str = str[i+1:]
    return tok, str

def handle_conn(conn):
    c_addr = str(clientAddress)
    print('Connected with ' + c_addr)
    message = conn.recv(2048).decode()
    nothing, message = advance(conn, message)
    if nothing != '':
        print('[WARNING]', c_addr + ': ignoring input:', nothing)

    # Boas Vindas
    conn.send('Olá! Bem-vindo! Qual o seu nome?;'.encode())

    nome, message = advance(conn, message)
    # Serviços
    services_msg = 'Certo, ' + nome + '! Como posso te ajudar?' \
        + '\nDigite o número que correnponde à opção desejada:' \
        + '\n1 - Agendar um horário de monitoria' \
        + '\n2 - Listar as próximas atividades de disciplina' \
        + '\n3 - E-mail do professor;'
    conn.send(services_msg.encode())

    tag, message = advance(conn, message)
    msg = None
    if tag == '1':
        # Agendar Monitoria
        msg = 'Para agendar uma monitoria basta enviar' \
            + ' um e-mail para cainafigueiredo@poli.uftj.br$'
    elif tag == '2':
        # Atividades Pendentes
        msg = 'Fique atento para as datas das próximas atividades.' \
            + '\nConfira por aí!\n' \
            + '\nP1: 26 de maio de 2022' \
            + '\nLista 3: 29 de maio de 2022$'
    elif tag == '3':
        # E-mail do Professor
        msg = 'Quer falar com o professor?' \
            + '\nO e-mail dele é sadoc@dcc.ufrj.br$'

    if msg != None:
        conn.send(msg.encode())

    # Finalizar
    fin_msg = '\nObrigado por utilizar nossos serviços!\nAté logo!$$'
    conn.send(fin_msg.encode())
    if message != '':
        print('[WARNING]', c_addr + ': ignoring trailing:', message)
    conn.close()
    print('Disconnecting ' + c_addr)

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
