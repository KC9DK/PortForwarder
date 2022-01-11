# !/usr/bin/env python3

'''
Python Simple Port Forwarder - by KC9DK 11 JAN 2022

Based on code by supernifty
https://github.com/supernifty/port-forwarder
'''

import socket

def forward(data, port, targetHost, targetPort):
	# print ("*** Forwarding: '%s' from port %s" % (data, port))
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.bind(("localhost", port)) # Bind to the port data came in on
	sock.sendto(data, (targetHost, targetPort))

def listen(host, port):
	listen_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	listen_socket.bind((host, port))
	print ("*** Listening on %s:%s\n" % ( host, port ))
	for port in target_port:
		if port != 0:
			print ("*** Forwarding to %s:%s\n" % ( target_host, port ))
	print('\n\nCLOSING THIS WINDOW WILL STOP FORWARDING AND CLOSE THE PORTS!')
	while True:
		data, addr = listen_socket.recvfrom(bufsize)
		for port in target_port:
			forward(data, addr[1], target_host, port) # data and port



if __name__ == "__main__":
	targetindex = 0
	target_port = [0] * 10

	with open("portdat.dat") as f:
		for line in f:
			if not line.strip().startswith('#'):
				(a,b) = line.split()
				if a == "listen_host":
					listen_host = b
				elif a == "listen_port":
					listen_port = int(b)
				elif a == "target_host":
					target_host = b
				elif a == "target_port":
					target_port[targetindex] = int(b)
					targetindex += 1

	bufsize = 2048
	print('### Python Simple Port Forwarder - by KC9DK ###\n')
	listen(listen_host, listen_port)

