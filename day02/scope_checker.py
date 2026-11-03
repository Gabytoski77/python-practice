# Day 2 - Scope Checker
scope_ip = "10.10.4.22"

target_ip = input("Enter target ip: ")

if target_ip == scope_ip:
    print("IN SCOPE - you have permission to test this target")
else:
    print("OUT OF SCOPE - do NOT test this target")

port =int (input("what is your port? "))

if port == 21:
    print("FTP - file transfer")
elif port == 22: 
    print("SSH - remote login")
elif port == 80:
    print("HTTP - website (not encrypted)")
elif port == 443: 
    print("HTTPS - website (encrypted)") 
else:
    print("Unknown service - investigate further") 


if port < 1024:
    print("This is a well known port")
else: 
    print("This is a high port")


