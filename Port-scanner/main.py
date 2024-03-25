import pyfiglet
import sys
import socket
import threading
from termcolor import colored
from datetime import datetime

def scan_port(ipaddr, port):

    try :

        SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        SOCKET.settimeout(1)
        STATUS = (ipaddr, port)
        SOCKET.connect(STATUS)
        SOCKET.close()
        print(colored(f"[+] Port Open {str(port)}", "green"))
    
    except :
        print(colored(f"[-] Port Closed {str(port)}", "red"))

def start_scan(target, ports=1000):

    print(colored(f"Starting Scanning {target}","light_yellow"))
    
    All_thread = []

    for port in range(ports):

        Thread = threading.Thread(target=scan_port, args=(target, port))
        All_thread.append(Thread)
        Thread.start()

    for t in All_thread:
        t.join()


ascii_head = pyfiglet.Figlet()
value = ascii_head.renderText("Port Scanner")
print(value)
print(f"Scanning started at: {str(datetime.now())}")
print("_"*50)
print("")

while True:
    print('''1) FOR MULTIPLE IP ADDRESS 
2) FOR SINGLE IP ADDRESS
3) quit''')
    print("_"*50)  
    print("")
    User = int(input("Enter: "))

    match User:
        case (1):
            Targets = list(map(str, input("Enter Ip Address: ").split(",")))
            print("*By default it scan 1000 ports")
            ports = int(input("Enter number of port you want to scan: "))
            for target in Targets:
                start_scan(target, ports)
        
        case (2):
            Target = input("Enter Target IP Address: ")
            # print("*By default it scan 1000 ports")
            Ports = int(input("Enter number of ports: "))
            start_scan(Target, Ports)
        
        case (3):
            print(colored("Thank you for using this! ..."))
            break
    
    print("")
    print("_"*50)
