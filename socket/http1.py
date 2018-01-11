import socket
#服务端，整个程序就是个套路
#服务器的host为空字符串，表示接受任意ip地址的连接，post是端口，端口1024以下的为操作系统预留，不可占用
host=''
port=2000
#s是一个socket实例
s=socket.socket()
#s.bind用于绑定，注意bind函数的参数是一个tuple
s.bind((host,port))
#需要先用s.listen开始监听

#用无限循环处理请求
while True:
    print('before listen')
    s.listen(5)
    print('before accept')
    connection,address=s.accept()
    print('after accept')
    #当有客户端过来连接时，s.accept函数返回两个值，分别是连接和客户端ip地址
    request=connection.recv(1024)
    #recb可以接收客户端发过来的数据，参数是要接收的字节数，返回值是一个bytes
    # print('ip and request,{}\n{}',format(address,request.decode(request)))
    #b''表示这是个bytes对象
    response=b'HTTP/1.1 233 OK \r\n\r\n<h1>hello<h1>'
    connection.sendall(response)
    #用sendall发给客户端
    connection.close()
    #发送完毕，关闭本次连接

    #客户端用connect,服务端用bind绑定端口，如果其端口未绑定而是随机分配，那么浏览器将不会知道用哪个端口访问


