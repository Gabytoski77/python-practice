# Day 3 - Loops.

ports = [21, 22, 80, 443, 3389, 8080] 

for port in ports: 
    if port == 21: 
        print(f"Port {port}: FTP - File transfer ")
    elif port == 22:
        print(f"Port {port}: SSH - Secure shell") 
    elif port == 80:
        print(f"Port {port}: HTTP - website (not encrypted)")
    elif port == 443: 
        print(f"Port {port}: HTTPS - website (encrypted)")
    elif port == 3389: 
        print(f"Port {port}: RDP - Windows remote desktop") 
    else: 
        print(f"Port {port}: Unknown service - investigate further")

    if port < 1024: 
        print("This is a well known port")
    else: 
        print("This is a high port") 
    print()


print("\n=== Login System ===")
correct_password = "Secure123"
attempts = 0 

while attempts < 3:
    password = input("Enter password: ") 
    if password == correct_password:
        print("Access granted") 
        break
    else:
        attempts += 1 
        print(f"Wrong password. Attempts left: {3 - attempts}")
if attempts == 3:
    print("ACCOUNT LOCKED - too many failed attempts") 
