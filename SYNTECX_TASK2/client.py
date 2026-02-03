import socket
import threading
from cryptography.fernet import Fernet

# Load the same key used by server
with open("secret.key", "rb") as key_file:
    KEY = key_file.read()

cipher = Fernet(KEY)

def receive_messages(client):
    while True:
        try:
            encrypted_msg = client.recv(1024)
            message = cipher.decrypt(encrypted_msg).decode()
            print(message)
        except:
            print("Connection closed.")
            break

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 5555))

    print("Connected to encrypted chat server")

    thread = threading.Thread(target=receive_messages, args=(client,))
    thread.start()

    while True:
        msg = input()
        encrypted_msg = cipher.encrypt(msg.encode())
        client.send(encrypted_msg)

start_client()