import socket

def netcat(hostname, port, content):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.send(bytes(content, 'UTF-8'))
    s.shutdown(socket.SHUT_WR)    


netcat('192.168.1.200',1729,'set salon on')