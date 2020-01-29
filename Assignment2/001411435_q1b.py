from socket import *

# socket to connect to ftp server
ftpSocket = socket(AF_INET, SOCK_STREAM)
ftpPort = 21

# socket for client to connect to
clientSocket = socket(AF_INET, SOCK_STREAM)
clientPort = 1234
clientSocket.bind((gethostname(), clientPort))
clientSocket.listen(1)
connection, address = clientSocket.accept()


# function to create ftp connection with server
def connect(command):
    ftpSocket.connect((command, ftpPort))
    reply = ftpSocket.recv(65565)
    return reply.decode("utf-8")


# wrapper to simulate http request. Note, I left out headers
def httpWrapper(command):
    return bytes("HTTP/1.1 " + command + "\r\n", "utf-8")


# function to "unwrap" incoming http message from server
def httpUnwrapper(command):
    lines = command.decode("utf-8").split(" ")
    return lines[-2]

with connection:
    print("Connected by", address)
    while True:
        print("Listening for commands from client...")
        data = connection.recv(1024)
        if not data:
            break
        command = httpUnwrapper(data)
        print("Command from client: " + command)
        if command == 'ftp.cdc.gov':
            # create connection with ftp server
            command = "ftp.cdc.gov"
            response = connect(command)
            connection.sendall(httpWrapper(response))
        elif command == "USER":
            command = b'USER anonymous\r\n'
            ftpSocket.sendall(command)
            response = ftpSocket.recv(1024).decode("utf-8")
            connection.sendall(httpWrapper(response))
        elif command == "PWD":
            command = b'PWD\r\n'
            ftpSocket.sendall(command)
            response = ftpSocket.recv(1024).decode("utf-8")
            connection.sendall(httpWrapper(response))
        elif command == "QUIT":
            command = b'QUIT\r\n'
            ftpSocket.sendall(command)
            response = ftpSocket.recv(1024).decode("utf-8")
            connection.sendall(httpWrapper(response))
        elif command == "SYST":
            command = b'SYST\r\n'
            ftpSocket.sendall(command)
            response = ftpSocket.recv(1024).decode("utf-8")
            connection.sendall(httpWrapper(response))
        elif command == "CWD":
            command = b'CWD \\\r\n'
            ftpSocket.sendall(command)
            response = ftpSocket.recv(1024).decode("utf-8")
            connection.sendall(httpWrapper(response))
        elif "@" in command:
            email = command
            command = bytes("PASS " + email + "\r\n", "utf-8")
            print(command)
            ftpSocket.sendall(command)
            response = ftpSocket.recv(1024).decode("utf-8")
            connection.sendall(httpWrapper(response))