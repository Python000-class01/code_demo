import socket

HOST = '192.168.2.110'
PORT = 60080

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind( (HOST, PORT) ) 
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print(f'Connected from {addr}')
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
