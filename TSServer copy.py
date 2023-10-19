from socket import *
import time
import threading

def handle_client(connectionSocket, addr):
    T2 = time.time() # Receive timestamp
    connectionSocket.recv(1024).decode()
    
    T3 = time.time() # Response time stamp
    # Sending Receive and Sending timestamps of server (T2 & T3)
    connectionSocket.send((str(T2) + '\t' + str(T3)).encode()) 
    connectionSocket.close()


serverPort = 11932           # Port is 10000 + last 4 digits of spire ID
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(10)

print('The server is ready to receive')

while True:
    connectionSocket, addr = serverSocket.accept()
    
    # Start a new thread that handles an incoming connection. Whereas this thread keeps on listening.
    client_thread = threading.Thread(target=handle_client, args=(connectionSocket, addr))
    client_thread.start()

