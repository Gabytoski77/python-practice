# Day 1 - Recon Target Card
hostname = "web01"
ip_address = "10.10.4.22"
open_ports = 3
cvss_score = 9.8
in_scope = True

print("=== Target Card ===")
print(f"Host: {hostname}")
print(f"IP: {ip_address}")
print(f"Open Ports: {open_ports}")
print(f"Highest CVSS: {cvss_score}")
print(f" In Scope: {in_scope}")
print(f"The type of open_ports is {type(open_ports)}")

