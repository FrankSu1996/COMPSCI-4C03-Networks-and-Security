from socket import *
serverName = 'Facebook'

# facebook.com ip address
serverIp = "31.13.80.36"
port = 1234

clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "Hello"
clientSocket.sendto(message.encode(), (serverIp, port))
