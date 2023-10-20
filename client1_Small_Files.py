# CS_372: SOCKETS AND HTTP - Program 1 (Using a socket to GET a file)
# Zachary Pilson
# pilsonz@oregonstate.edu

# imported libraries 
from socket import * 

# Constants
HOST = "gaia.cs.umass.edu"
HTTP_PORT = 80
ADDRESS = (HOST, HTTP_PORT)
HTTP_COMPLIANT = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
SIZE = 1024

######################################################################################################
## Knowledge Retrieved from: https://www.internalpointers.com/post/making-http-requests-sockets-python
## Purpose: Creates a socket object, then connects to an address
## AF_INET - IPv4 addresses
## SOCK_STREAM - "Stream-based protocol because of TCP"
## address - (IP, PORT) - IP is retrieved automatically by .connect using DNS lookup
## Returns: Socket object
######################################################################################################
def createSocketConnection(address):
    sockObj = socket(AF_INET, SOCK_STREAM)
    sockObj.connect(address)
    return sockObj

######################################################################################################
## Knowledge Retrieved from: https://www.internalpointers.com/post/making-http-requests-sockets-python
## Purpose: Request and recieve data from server
## SIZE - constant for maximum recieved bytes
## Returns: decoded response
######################################################################################################
def requestData(sockObj, http_compliant):
    sockObj.send(http_compliant.encode('UTF-8'))
    response = sockObj.recv(SIZE)
    return response.decode('UTF-8')

######################################################################################################
## Knowledge Retrieved from: https://www.internalpointers.com/post/making-http-requests-sockets-python
## Purpose: Closes a socket
## Returns: None
######################################################################################################
def closeSocket(sockObj):
    sockObj.close()

if __name__ == "__main__":

    # Displays Request + Host (for screenshot completion)
    print(f'Request: {HTTP_COMPLIANT}')
    
    # Creates a socket object and establishes a connection to host ("gaia.cs.umass.edu")
    mySocket = createSocketConnection(ADDRESS)

    # Sends GET request and accepts returned data
    data = requestData(mySocket, HTTP_COMPLIANT)

    # Displays data length in bytes and HTTP response (for screenshot completion)
    print(f'[RECV] - length: {len(data)}\n{data}')

    # Close socket connection
    closeSocket(mySocket)