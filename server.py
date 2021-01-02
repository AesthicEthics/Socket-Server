import socket

#------------Server Side-----------------#
def recvall(sock):
    BUFF_SIZE = 4096 # 4 KiB
    data = b''
    while True:
        part = s.recv(BUFF_SIZE)
        data += part
        if len(part) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data
#-----------^Experimental^---------------#
c = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = '0.0.0.0'
PORT = 65432

s.bind(((HOST),(PORT)))
s.listen()
print("Now listening for connections")
while(True):
    (clientConnected, clientAddress) = s.accept()
    print(("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1])))

    dfc = clientConnected.recvall(s)
    dtc = dfc.decode()
    c.append(dtc)

print(c)
#-----------------AES----------Decryption----------------#
