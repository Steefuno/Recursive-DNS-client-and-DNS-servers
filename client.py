import threading
import socket
import sys
import re

fileName = "PROJI-HNS.txt"
resolved = open("RESOLVED.txt", "w+")

def TShandler(query, tsHostname, tsListenPort):
	
	try:
		clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[C]: Client socket created")
	except socket.error as error:
		print('socket open error:...')
		exit()

	#connect to server
	server_binding = (socket.gethostbyname(tsHostname), tsListenPort)
	clientSocket2.connect(server_binding)
	
	#send the query (hostname) as a string to TS
	clientSocket2.send(query) 
	
	#receive and write to the file
	data = clientSocket2.recv(256)	
	n = resolved.write(data + '\n')
	
	return

def handleRSreply(query, data, tsListenPort):
	words = data.split()
	flag = re.search(r"\w+", words[2]).group()
	
	if flag == "A":
		#this means entry was a match
		#print and put into resolved
		n = resolved.write(data + '\n')
	else:
		#this means entry was not a match
		#have to connect to TS
		tsHostname = words[0]
		TShandler(query, tsHostname, tsListenPort) 	

	return	

def findHosts(clientSocket,tsListenPort):
	#Send PROJI-HNS.txt one line at a time to server and receive (IP and A) or (NS)
	fileObject = open(fileName, "r")
	for line in fileObject:
		print("Sending <" + line + ">");
		clientSocket.send(line)
		data = clientSocket.recv(256)
		print("Received " + data)
		handleRSreply(line, data, tsListenPort)

	fileObject.close()
	return

def main():
	#client takes in rsHostname rsListenPort tsListenPort
	if len(sys.argv) != 4:
		print("Invalid Input\n")
		exit()

	if not sys.argv[2].isdigit() or not sys.argv[3].isdigit():
		print("Invalid Input\n")
		exit()

	rsHostname = sys.argv[1]
	rsListenPort = int(sys.argv[2])
	tsListenPort = int(sys.argv[3])

	try:
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[C]: Client socket created")
	except socket.error as err:
		print('socket open error: {} \n'.format(err))
		exit()

	# connect to the server on local machine
	server_binding = (socket.gethostbyname(rsHostname), rsListenPort)
	clientSocket.connect(server_binding)

	findHosts(clientSocket, tsListenPort)
	
	#closing message
	clientSocket.send("My milkshakes bring all the boys to the yard")
	clientSocket.close()
	exit()

main()
