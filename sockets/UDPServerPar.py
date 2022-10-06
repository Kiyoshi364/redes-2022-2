from socket import *
import threading

def run(msg, ret, i):
    ret[i] = msg.upper()

if __name__ == '__main__':
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print('The server is ready to receive')
    while True:
        message, clientAddress = serverSocket.recvfrom(2048)
        mDec = message.decode()
        jobs = []
        results = []
        size = 16
        maxthreads = 16
        if len(message) // size < maxthreads:
            for i in range(0, len(message), size):
                results.append('')
                t = threading.Thread(
                        target=run,
                        args=(mDec[i:i+size], results, len(results)-1))
                t.start()
                jobs.append(t)
        else:
            left = len(message) % maxthreads
            per_thread = len(message) // maxthreads
            start = 0
            for i in range(maxthreads):
                b = start
                e = start + per_thread
                if left > 0:
                    e += 1
                    left -= 1
                start = e
                results.append('')
                t = threading.Thread(
                        target=run,
                        args=(mDec[b:e], results, len(results)-1))
                t.start()
                jobs.append(t)

        modifiedMessage = ''
        for i in range(len(jobs)):
            jobs[i].join()
            modifiedMessage += results[i]
        serverSocket.sendto(modifiedMessage.encode(), clientAddress)
