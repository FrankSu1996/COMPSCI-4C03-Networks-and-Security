from socket import *

port = 1234
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.connect((gethostname(), port))


# wrapper to simulate http request. Note, I left out headers
def httpWrapper(command):
    return bytes("GET " + command + " HTTP/1.1\r\n", "utf-8")

# function to "unwrap" incoming http message from server
def httpUnwrapper(command):
    # gets rid of "HTTP/1.1"
    return command.split(None, 1)[1]

# Initial print message
print("To create an ftp connection, please enter the following command: 'ftp ftp.cdc.gov' and press enter:")

# infinite loop to receive commands from user input
while True:
    command = input()
    if command == "ftp ftp.cdc.gov":
        wrappedCommand = httpWrapper(command)
        serverSocket.sendall(wrappedCommand)
        response = serverSocket.recv(1024)
        print(httpUnwrapper(response.decode("utf-8")))
        print("""You can now use the following commands:
            USER
            PASS
            PWD
            CWD
            HELP
            CDUP
            SYST
            QUIT
            """)
    elif command == "USER":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))
    elif "PASS" in command:
        command = bytes("POST " + command + " \r\n", "utf-8")
        serverSocket.sendall(command)
        response = serverSocket.recv(1024).decode("utf-8")
        print("Response from server:")
        print(response)
    elif command == "PWD":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))
    elif command == "QUIT":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))
    elif command == "SYST":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))
    elif command == "CWD":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))
    elif command == "HELP":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))
    elif command == "CDUP":
        serverSocket.sendall(httpWrapper(command))
        response = serverSocket.recv(1024)
        print("Response from server:")
        print(httpUnwrapper(response.decode("utf-8")))