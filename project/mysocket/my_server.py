from socket import *
BUFSIZE = 1024

#1.开启server  2.监听端口   3读取数据  4.回复数据  5关闭socket
socketServer = socket(AF_INET, SOCK_STREAM)
socketServer.bind(('',6900))

socketServer.listen(5)

print("socket 开启")
#读取数据
while True:
    client, c_addr = socketServer.accept()

    print("receive data from client:")
    while True:
        data = client.recv(BUFSIZE)
        if data:
            print('client:', data.decode('utf-8') )
            #回复稍息
            buf = input('please input something to client')
            client.send(buf.encode('utf-8'))
        else:
            print('connect shut down from client ',c_addr)
            break
    #关闭客户端套接字
    client.close()
socketServer.close()



