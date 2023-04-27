import socket
import hashlib

SERVER_HOST = '127.0.0.1' 
SERVER_PORT = 65434  


PROXY_HOST = '127.0.0.1'  
PROXY_PORT = 8081       

# Connect to the diode over TCP
s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.connect((SERVER_HOST, SERVER_PORT))
print("Connected to server.")

# Listen for incoming connections from the proxy
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_sock:
    proxy_sock.bind((PROXY_HOST, PROXY_PORT))
    proxy_sock.listen()
    print('Waiting for a proxy to connect...')
    conn, addr = proxy_sock.accept()
    print('Connected by', addr)

    # Create an empty buffer to store the incoming chunks
    buffer = b''

    # Loop until all data has been received
    while True:
        # Receive data in 1KB chunks
        data = conn.recv(4096)
        s_sock.sendall(data)
        # Break out of the loop if no more data is received
        if not data:
            break

        # Concatenate the incoming chunk with the buffer
        buffer += data

    # Print the forwarded data
    md5_hash = hashlib.md5(buffer).hexdigest()
    print(f"MD5 hash of file: {md5_hash}")
    #print('Forwarded data:', buffer.decode('utf-8'))
    print('File forwarded to destination through the diode.')

