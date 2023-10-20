# CS_372: SOCKETS AND HTTP - Program 3 (The world's simplest HTTP server)
# Zachary Pilson
# pilsonz@oregonstate.edu

# imported libraries 
from socket import * 

# Constants
HOST = '127.0.0.1'
RANDOM_PORT = 4321
ADDRESS = (HOST, RANDOM_PORT)
DATA = "HTTP/1.1 200 OK\r\n"\
 "Content-Type: text/html; charset=UTF-8\r\n\r\n"\
 "<html>Congratulations! You've downloaded the first Wireshark lab file!</html>\r\n"
SIZE = 1024

######################################################################################################
## Knowledge Retrieved from: https://www.internalpointers.com/post/making-http-requests-sockets-python
## Purpose: Runs this server for ONLY 1 client. The connection will be closed after sending data.
## NOTE: I was going to have the server run infinitely (with While loop), 
##       but the screenshot suggests it should only run once before closing.
## AF_INET - IPv4 addresses
## SOCK_STREAM - "Stream-based protocol because of TCP"
## Returns: None
######################################################################################################
def runningServer():
    # Creates, binds, and then listens for client activity
    serverObj = socket(AF_INET, SOCK_STREAM)
    serverObj.bind(ADDRESS)
    serverObj.listen()

    # Awaiting to accept clients
    clientConnection, clientAddr = serverObj.accept()

    # Printing client information, and then sending data to client
    print(f'Connected by {clientAddr}\n\nReceived: {clientConnection.recv(SIZE)}\n\nSending>>>>>>>>\n{DATA}\n<<<<<<<<')
    clientConnection.send(DATA.encode('UTF-8'))

    # Disconnecting client and closing server
    clientConnection.close()
    serverObj.close()
        
        
if __name__ == "__main__":
    runningServer()
