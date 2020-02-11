# Echo client program
import socket

HOST = 'localhost'    # The remote host
PORT = 50009          # The port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

def wrapper(str):
    return bytes("GET " + str + " HTTP/1.1\r\n\r\n", 'utf-8')

def unwrapper(str):
    return str.split(None, 1)[1] #delete the "HTTP/1.1 " part

while True:
    cmd = input()
    if cmd == "ftp ftp.cdc.gov" or cmd == "1": # 1 for testing
        #str = cmd.split()[1]
        str = "ftp ftp.cdc.gov"
        s.sendall(wrapper(str))
        reply = s.recv(65565)
        print(unwrapper(reply.decode("utf-8")))
    elif cmd == "USER":
        m = 'USER'
        s.sendall(wrapper(m))
        reply = s.recv(65565)
        print(unwrapper(reply.decode("utf-8")))
    elif cmd == "HELP":
        m=b"HELP\r\n"
        help(m)
    elif "PASS" in cmd:
        m = bytes(cmd+"\r\n", 'utf-8')
        password(m)

s.sendall(b'Hello, world')
data = s.recv(1024)
print('Received', repr(data))