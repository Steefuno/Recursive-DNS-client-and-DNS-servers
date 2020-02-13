import threading
import time
import random
import socket

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


def main():
	#client takes in rsHostname rsListenPort tsListenPort
	#parse these arguments
	
	
	

if __name__ == "__main__":
	main()
