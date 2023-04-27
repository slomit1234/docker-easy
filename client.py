import socket
import hashlib
HOST = '127.0.0.1'  # IP address of the server
PORT = 65432       # Port to connect to

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    buffer = b''
    with open('test.txt', 'rb') as f:
        while True:
            data = f.read(4096)  # read file data in 1KB chunks
            if not data:
                break
            buffer += data
            s.sendall(data)      # send data to server

    md5_hash = hashlib.md5(buffer).hexdigest()
    print(f"MD5 hash of file: {md5_hash}")
    print('File transfer completed!')

