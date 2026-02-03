import socket
import threading
from cryptography.fernet import Fernet
from datetime import datetime

# Generate key (same key must be used by clients)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

clients = []
lock = threading.Lock()

# Save key to file (for demo purpose)
with open("secret.key", "wb") as key_file:
    key_file.write(KEY)

def log_message(message):
    with open("chat_log.txt", "a") as file:
        file.write(message + "\n")

def handle_client(client_socket, address):
    print(f"[CONNECTED] {address}")

    while True:
        try:
            encrypted_msg = client_socket.recv(1024)
            if not encrypted_msg:
                break

            message = cipher.decrypt(encrypted_msg).decode()
            timestamp = datetime.now().strftime("%H:%M:%S")
            final_msg = f"[{timestamp}] {address}: {message}"

            print(final_msg)
            log_message(final_msg)

            broadcast(encrypted_msg, client_socket)

        except:
            break

    with lock:
        clients.remove(client_socket)
    client_socket.close()
    print(f"[DISCONNECTED] {address}")

def broadcast(message, sender_socket):
    with lock:
        for client in clients:
            if client != sender_socket:
                client.send(message)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5555))
    server.listen()

    print("🔐 Encrypted Chat Server Started")
    print("Waiting for clients...")

    while True:
        client_socket, address = server.accept()
        clients.append(client_socket)

        thread = threading.Thread(
            target=handle_client,
            args=(client_socket, address)
        )
        thread.start()

start_server()