from termcolor import colored
import socket
import time



def scan_port(ipaddr, port):

    try:
        SOCKET = socket.socket()
        STATUS = (ipaddr, port)
        SOCKET.connect(STATUS)
        SOCKET.close()
        print(colored(f"[+] Port Opened {str(port)}","green"))
    
    except:
        print(colored(f"[-] Port Closed {str(port)}", "red"))



def start_scan(target, ports):

    for i in range(2):
        time.sleep(1)
        print("STARTING....")
    print("")
    print(colored(f'''STARTING SCANING {target}'''))
    for port in range(ports):
        print(colored(f"SCANNING PORT {port}", "yellow"))
        scan_port(target, port)

print(colored("Welcome to port scanner", "black"))
print(colored(f"1. Single Target", "black"))
print(colored(f"2. Multiple Target", "black"))

user = int(input("Enter: "))

if user == 1:

    TARGET = input("ENTER IP ADDRESS: ")
    PORTS = int(input("ENTER NUMBER OF PORTS: "))
    start_scan(TARGET, PORTS)


elif user == 2:

    TARGETS = list(map(str, input("ENTER ALL IP ADDRESS: ").split(",")))
    PORTS = int(input("ENTER NUMBER OF PORTS: "))
    for target in TARGETS:
        start_scan(target, PORTS)
        # print(target)



else :
    print(colored("TRY FOR A VALID INPUT!","light_red"))





