from socket import *
from datetime import datetime, timezone
import time
import sys


def main(serverName):
    serverPort = 11932                                  # Server's Port (10000 + Spire ID last 4 digits)
    # serverName = 'localhost'

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName,serverPort))
    T1 = time.time()    
    clientSocket.send("Hello".encode())                 # First message to the Server. 
    serverResponse = clientSocket.recv(1024)            # Server's Response is a a tab seperated message having T2 & T3
    T4 = time.time()

    T2 = float(serverResponse.decode().split()[0])
    T3 = float(serverResponse.decode().split()[1])


    RTT = int(((T2 - T1) + (T4 - T3) ) * 1000)          # RTT = round trip time = ping time
    print(f"REMOTE_TIME {int(T3*1000) + int(RTT/2)}")   # Remote Time means an estimate of the current time at Server side. 
    print(f"LOCAL_TIME {int(T4*1000)}")
    print(f"RTT_ESTIMATE {RTT}")


    clientSocket.close()

if __name__ == "__main__":
    if(len(sys.argv) == 2):
        main(str(sys.argv[1]))

    else:
        print("Wrong usage. Run $python TSClient.py <host_ip_addr>")