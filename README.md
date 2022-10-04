# Simple python socket_ssl

### Generate the certificates for the server
`openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server.key -out server.crt -subj "/CN=<YOUR DOMAIN>"`

### Generate the certificates for the client
`openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout client.key -out client.crt -subj "/CN=Client"`

### Add the server.[crt|key] and client.[crt|key] keys in their respective folders

### Run Server
`python3 server.py`

### Run Client
`python3 client.py`

#### have a fun ;)