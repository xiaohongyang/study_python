from socket import *
import socket

SOCKET_PORT = 6900
BUFSIZE = 1024

# 1.创建client  2.连接socket服务器 3.输入数据   4.接收数据   5.关闭client
client = socket.socket(AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', SOCKET_PORT))

while True:
    data = input("please input data:")
    if data != 'quit':
        client.send(data.encode('utf-8'))
        receiveData = client.recv(BUFSIZE)
        print("data from server:", receiveData.decode('utf-8'))
    else:
        break

client.close()