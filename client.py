import os
import socket

SERVER_HOST = os.environ['SERVER_HOST']
SERVER_PORT = int(os.environ['SERVER_PORT'])

filename = input('Enter the filename to send: ')
if os.path.exists(filename):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(filename.encode())
        with open(filename, 'rb') as f:
            while True:
                data = f.read(1024)
                if not data:
                    break
                s.sendall(data)
        print('File sent successfully.')
else:
    print('File does not exist.')

