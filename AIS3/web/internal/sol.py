import socket

def send_request(host, port, path):
    request = f"GET {path} HTTP/1.1\r\nHost: {host}\r\n\r\n"
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(request.encode())
        while True:
            response = s.recv(4096)
            print(response)
    return response

if __name__ == "__main__":
    host = "10.105.0.21"
    port = 11952
    path = "/?redir=http://localhost:7778"

    response = send_request(host, port, path)
    print(response)
