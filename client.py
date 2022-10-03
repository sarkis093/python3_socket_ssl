from base64 import encode
import socket
import sys
import ssl

host = "0.0.0.0"
port = 8080

purpose = ssl.Purpose.SERVER_AUTH
context = ssl.create_default_context(purpose, cafile='./server/server.crt')
context.load_cert_chain(certfile='./client/client.crt', keyfile='./client/client.key')

raw_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ssl_sock = context.wrap_socket(raw_sock, server_side=False, server_hostname='www.server.com.br')
ssl_sock.connect((host, port))

while True:
  prhase = input('command:> ')
  ssl_sock.send(prhase.encode('ascii'))
  data = ssl_sock.recv(4096).decode('ascii')
  print(data)
  if 'quit' in data: break
  
ssl_sock.close()