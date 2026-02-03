# Task 2 – Encrypted Chat App (AES)

## Description
This project is developed as **Task 2** of the **Syntecxhub Internship Program**.  
It is a **client-server encrypted chat application** built in Python where all messages are encrypted using **AES (symmetric encryption)** before being sent over the network.

The goal of this project is to demonstrate secure communication using encryption, socket programming, and basic concurrency.

---

## Features
- Client–Server chat application
- Messages encrypted using AES (Fernet)
- TCP socket communication
- Supports multiple clients using threading
- Encrypted messages before sending
- Decrypted messages on receiving
- Message logging on server side
- Basic error handling

---

## Technologies Used
- Python
- Socket Programming (TCP)
- AES Encryption (cryptography library)
- Multithreading

---

## How It Works
1. The server generates a **secret key** for encryption.
2. Clients use the same key to encrypt messages before sending.
3. Encrypted messages are sent to the server.
4. The server decrypts and logs messages, then broadcasts them.
5. Clients decrypt received messages and display them.

---

## How to Run the Project

### Step 1: Install Dependency
```bash
pip install cryptography
Step 2: Start the Server
python server.py
Step 3: Start Clients (in separate terminals)
python client.py
You can run multiple clients to test chat functionality.
Files Included
server.py – Server-side code
client.py – Client-side code
secret.key – Encryption key (for demo purpose)
chat_log.txt – Logged chat messages
README.md – Project documentation
Key Management & Security Note
For demonstration purposes, the encryption key is stored locally in a file.
In real-world applications, secure key exchange mechanisms and protected storage should be used, as storing keys locally can be a security risk.