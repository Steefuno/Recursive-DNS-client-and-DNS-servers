import threading
import socket
import sys

fileName = "PROJI-HNS.txt"
resolved = open("RESOLVED.txt", "w+")
#Protocol

#need two sockets: for rs and ts
#client first connects to RS
	#send hostname as a string to RS
	
#---------------------SERVER SIDE-------------------------------------------
#RS:
#maintain DNS with these 3 fields  Hostname, IP address, Flag (A or NS)
#what data structures can we use?
	#Linked list with the 3 fields in each node?
	#	
#RS program does a lookup in it's DNS table
		#if match: sends this entry as a string to the client: Hostname IPaddress A
		#if no match: RS sends this string to client: TSHostname - NS
			#TSHostname is the name of the machine on which the TS program is running

#TS:
#TS program looks up hostname
	#if match: sends this entry as a string to the client: Hostname IPaddress A
	#if no match: sends error string: Hostname - Error:HOST NOT FOUND

#------------------------------------------------------------------------		
#if client receives:
	#string with A field: output received string as is
	#string with NS field: uses TSHostname to determine IP address of machine running the TS program
	#connect to TS program using second socket 
	#client sends queried hostname as a string to TS

def TShandler(tsHostname,tsListenPort):
	
	try:
		clientSocket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("[C]: Client socket created")
	except socket.error as error:
		print('socket open error:...')
		exit

	#connect to server
	
	server_binding = (tsHostname, tsListenPort)
	clientSocket2.connect(server_binding)
	
	#send the query (hostname) as a string to TS

	return

def handleRSreply(data, tsListenPort):
	words = data.split()
	flag = re.search(r"\w+", words[2]).group()
	
	if flag == "A":
		#this means entry was a match
		#print and put into resolved
		n = resolved.write(data+ '\n')
		
	else:
		#this means entry was not a match
		#have to connect to TS
		tsHN = words[0]
		TShandler(tsHN, tsListenPort) 	
	
	return	

def findHosts(clientSocket,tsListenPort):
	#Send PROJI-HNS.txt one line at a time to server and receive (IP and A) or (NS)
	
	fileObject = open(fileName, "r")
	line = fileObject.readline() 
 		
	while line:
	#check out how this works	
		clientSocket.send("fileObject.readline()")
		data = clientSocket.recv(256)
		print("Received " + data)
		handleRSreply(data,tsListenPort)	

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
	server_binding = (rsHostname, rsListenPort)
	clientSocket.connect(server_binding)

	findHosts(clientSocket, tsListenPort)
	
	clientSocket.close()
	exit()

main()
