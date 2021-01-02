import pyaes, pbkdf2, binascii, os, secrets, socket, struct

password = "s3cr3t*c0d3"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)

iv = secrets.randbits(256)
plaintext = "Text for encryption"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(plaintext)
finaltext =  binascii.hexlify(ciphertext)

arr = [str(key),str(iv),str(ciphertext)]

#-------------Socket Programming Starts------------------------#

def send_msg(sock, msg):
    # Prefix each message with a 4-byte length (network byte order)
    msg = struct.pack('>I', len(msg)) + msg
    sock.sendall(msg)

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = '192.168.0.19'
PORT = 65432
s.connect(((HOST),(PORT)))

while True:
    for i in range(len(arr)):
        data = arr[i]
        data2 = data.encode()
        send_msg(s, data2)
