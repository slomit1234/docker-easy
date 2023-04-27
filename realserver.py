import socket
import hashlib

SERVER_HOST = '127.0.0.1'  # IP address of the proxy
SERVER_PORT = 65434      # Port to listen on

# Listen for incoming connections from the proxy
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s_sock:
    s_sock.bind((SERVER_HOST, SERVER_PORT))
    s_sock.listen()
    print('Waiting for a diode to connect...')
    conn, addr = s_sock.accept()
    #print (type(addr))
    #print (addr)
    print('Connected by', addr)
    if (addr[0] ==  '127.0.0.1'): #change to the diode address
    
        # Create an empty buffer to store the incoming chunks
        buffer = b''

        # Loop until all data has been received
        while True:
            # Receive data in 1KB chunks
            data = conn.recv(4096)

            # Break out of the loop if no more data is received
            if not data:
                break

            # Concatenate the incoming chunk with the buffer
            buffer += data

        # Write the concatenated data to a file
        with open('received_file', 'wb') as f:
            f.write(buffer)

        # Print the forwarded data
        md5_hash = hashlib.md5(buffer).hexdigest()
        print(f"MD5 hash of file: {md5_hash}")
        #print('Forwarded data:', buffer.decode('utf-8'))
        print('File forwarded to destination through the diode.')
    
    
