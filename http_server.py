import socket

from concurrent.futures import ThreadPoolExecutor


t = ThreadPoolExecutor(5)

# 默认是tcp协议
server = socket.socket()
server.bind(('0.0.0.0', 8000))
server.listen()


# 对每个请求的处理
def handle_sock(_sock, addr):
    data = ""
    while True:
        tmp_data_json = _sock.recv(1024)
        tmp_data = tmp_data_json.decode('utf-8')
        # http响应
        response_template = '''HTTP/1.1 200 OK

<html>
<head><title>hhhh</title></head>
<body><h1>hello</h1></body>
</html>

'''
        # 本身是字符串，无需json.dumps转字符串
        _sock.send(response_template.encode('utf-8'))
        _sock.close()


# 不断接受客户端请求，并新开线程处理
while True:
    # server负责接受连接请求，sock负责具体的数据传输，而addr则提供了客户端的地址信息（ip、端口
    # 阻塞方法，如果客户端close服务端会接收并取消阻塞
    sock, addr = server.accept()
    print('client is connected...')
    t.submit(handle_sock, sock, addr)


# sock.close()




