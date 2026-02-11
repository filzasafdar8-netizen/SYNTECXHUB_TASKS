import json

# Simulated services
services = {
    "nginx": "1.18.0",
    "openssl": "1.1.1",
    "apache": "2.4.46"
}

# Simulated CVE database
cve_db = {
    "nginx 1.18.0": ["CVE-2021-23017: High", "CVE-2020-35464: Medium"],
    "openssl 1.1.1": ["CVE-2021-3450: High"],
    "apache 2.4.46": []
}

# Scan simulation
for service, version in services.items():
    key = f"{service} {version}"
    print(f"Scanning {key}...")
    if key in cve_db and cve_db[key]:
        print("Possible CVEs found:")
        for cve in cve_db[key]:
            print(f" - {cve}")
    else:
        print("No known CVEs")
    print("-" * 40)