
import socket
import threading


class Client:
 
 def send_message():
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

server_host = '127.0.0.1'
server_port = 5555

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_host, server_port))

send_thread = threading.Thread(target=Client.send_message)
send_thread.start()

while True:
    data = client_socket.recv(1024)
    print("Server Message: " + data.decode('utf-8'))
