import socket
import threading
from datetime import datetime

# Lock for clean printing
print_lock = threading.Lock()

# Scan a single port
def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))

        with print_lock:
            if result == 0:
                print(f"[OPEN] Port {port}")
                log_result(f"Port {port} is OPEN")
            else:
                print(f"[CLOSED] Port {port}")
                log_result(f"Port {port} is CLOSED")

        sock.close()

    except Exception as e:
        with print_lock:
            print(f"[ERROR] Port {port}: {e}")
            log_result(f"Port {port} ERROR: {e}")

# Save results to file
def log_result(message):
    with open("scan_results.txt", "a") as file:
        file.write(message + "\n")

# Main function
def main():
    target = input("Enter target IP or hostname: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    print("-" * 50)
    print(f"Scanning target: {target}")
    print(f"Started at: {datetime.now()}")
    print("-" * 50)

    threads = []

    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_port, args=(target, port))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("-" * 50)
    print("Scan completed.")
    print(f"Finished at: {datetime.now()}")

if __name__ == "__main__":
    main()