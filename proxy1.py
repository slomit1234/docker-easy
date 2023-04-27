import socket
import hashlib

DIODE_HOST = '127.0.0.1'  # IP address of the diode
DIODE_PORT = 8081       # Port to connect to the diode

PROXY_HOST = '127.0.0.1'  # IP address of the proxy
PROXY_PORT = 65432       # Port to listen on

# Connect to the diode over TCP
diode_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
diode_sock.connect((DIODE_HOST, DIODE_PORT))
print("Connected to diode.")

# Listen for incoming connections from the client
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_sock:
    proxy_sock.bind((PROXY_HOST, PROXY_PORT))
    proxy_sock.listen()
    print('Waiting for a client to connect...')
    conn, addr = proxy_sock.accept()
    print('Connected by', addr)

    # Create an empty buffer to store the incoming chunks
    buffer = b''

    # Loop until all data has been received
    while True:
        # Receive data in 1KB chunks
        data = conn.recv(4096)
        
        # Send data to the diode over TCP
        diode_sock.sendall(data)

        # Break out of the loop if no more data is received
        if not data:
            break

        # Concatenate the incoming chunk with the buffer
        buffer += data

    # Write the concatenated data to a file
    with open('received_file', 'wb') as f:
        f.write(buffer)

    # Print the received data
    #print('Received data:', buffer.decode('utf-8'))
    md5_hash = hashlib.md5(buffer).hexdigest()
    print(f"MD5 hash of file: {md5_hash}")
    print('File transfer completed!')
