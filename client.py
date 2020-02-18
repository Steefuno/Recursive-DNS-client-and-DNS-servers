import threading
import socket
import sys

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
		#if no match: RS sends this string to client: TSHostname -NS
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

def findHosts(clientSocket):
	#Send PROJI-HNS.txt one line at a time to server and receive (IP and A) or (NS)
	clientSocket.send("google.com")

	data = clientSocket.recv(256)
	print("Received " + data)
	#repeat this for .txt file

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

	findHosts(clientSocket)
	
	clientSocket.close()
	exit()

main()
