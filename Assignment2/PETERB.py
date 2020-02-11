import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def init(str):  
    s.connect ((str,21))
    reply = s.recv(65565)
    return reply.decode("utf-8")
    #print("you can now use the following commands:")
    #print("USER")
    #print("HELP")
    #print("PASS example@chrome.com")

def help(message):
    s.sendall(message)
    reply = s.recv(65565)
    print(reply.decode("utf-8"))

def user(message):
    s.sendall(message)
    reply = s.recv(65565)
    return reply.decode("utf-8")

def password(message):
    s.sendall(message)
    reply = s.recv(65565)
    print(reply.decode("utf-8"))

HOST = "localhost"
PORT = 50009

def wrapper(str):
    str = "HTTP/1.1 " + str + "\r\n"
    return bytes(str, 'utf-8')

def unwrapper(str):
    lines = str.decode("utf-8").split(" ")
    res = ""
    for i in range(1, len(lines)-1):
        res += lines[i] + " "
    return res[:-1]


ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind((HOST,PORT))
ss.listen(1)
conn, addr = ss.accept()
with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(1024)
        if not data: break
        cmd = unwrapper(data)
        #print(cmd)
        if cmd == "ftp ftp.cdc.gov": 
            str = cmd.split()[1]
            reply = init(str)
            conn.sendall(wrapper(reply))
        elif cmd == "USER":
            m = b'USER anonymous\r\n'
            reply = user(m)
            conn.sendall(wrapper(reply))
        elif cmd == "HELP":
            m=b"HELP\r\n"
            help(m)
        elif "PASS" in cmd:
            m = bytes(cmd+"\r\n", 'utf-8')
            password(m)
        
