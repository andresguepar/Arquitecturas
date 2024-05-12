
import socket
import threading


class Server:

 def handle_client(client_socket, client_address):
    print(f"Conexión establecida con {client_address}")

    while True:
      
        data = client_socket.recv(1024)
        if not data:
            break
    
        for client in clients:
            if client != client_socket:
                client.send(data)

    client_socket.close()
    print(f"Conexión cerrada con {client_address}")


server_host = '127.0.0.1'
server_port = 5555


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((server_host, server_port))
server.listen(5)

print(f"Servidor escuchando en {server_host}:{server_port}")

clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)
    client_thread = threading.Thread(target=Server.handle_client, args=(client_socket, client_address))
    client_thread.start()