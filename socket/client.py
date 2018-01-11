# coding: utf-8
import socket
#socket 是操作系统用来进行网络通信的底层方案
#创建socket对象
#socket,AF_INET表示ipv4协议，socket.SOCK_STREAM 表示是tcp协议,这两个都是默认参数，可以不用写
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#可以写成 s=socket.socket(),只能连接http
#s=ssl.wrap_socket(socket.socket()) 能连接https,引入ssl库
#主机（域名或ip)和端口
host='localhost'
port=2000
#用connect函数连接上主机，参数是一个tuple
s.connect((host,port))

#连接后通过，以下函数得到本机的ip和端口
ip,port=s.getsockname()
print('本机ip和port{}{}'.format(ip,port))
http_request='GET /HTTP/1.1\r\nhost:{}\r\n\r\n'.format(host)
request=http_request.encode('utf-8')
print('请求',request)
s.send(request)
#发送http请求给服务器，send函数只接受bytes作为参数，str.encode把str转换成bytes,编码为utf-8

#接受服务器响应数据，参数是长度，这里为1023字节，所以这里如果返回数据超过1023部分就得不到了
response=s.recv(1023)
#输出响应数据，bytes类型
print('响应',response)
#转成str再输出
print('响应的str格式',response.decode('utf-8'))