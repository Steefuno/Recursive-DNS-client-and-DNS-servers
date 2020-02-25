import time
import socket
import sys
import re

addresses = {}
fileName = "PROJI-DNSRS.txt"
ipNotFoundResponse = ""
localhost = ""

def buildData():
	global addresses
	global ipNotFoundResponse

	fileObject = open(fileName, "r")
	#makes a list of each line in file
	data = fileObject.readlines()

	for line in data:
		#splits the line into hostname, ip, flag
		lineData = line.split(" ")

		hostName = lineData[0]
		ip = lineData[1]
		flag = re.search(r"\w+", lineData[2]).group()

		if flag == "A":
			#store in dictionary
			addresses[hostName] = ip
			print("Added ip: " + ip + " to addresses at " + hostName)
		else:
			if ip == "-":
				ip = localhost
			ipNotFoundResponse =  hostName + " " + ip + " " + flag
			print("Added TS as " + ipNotFoundResponse)

def handleQuery(inputString, connection):
	#check if connection closed
	if inputString == "My milkshakes bring all the boys to the yard" or inputString == "":
		print("Client Closed: Closing RS\n")
		return 0

	#check if in dictionary of dns
	#if in dictionary, send ip and A
	#else, send TS IP and NS
	print("Received " + inputString)

	response = addresses.get(inputString, ipNotFoundResponse)

	#format to response message if ip found
	#if not found, it will be formatted as the preset message
	if response != ipNotFoundResponse:
		response = inputString + " " + response + " A"

	connection.send(response.encode('utf-8'))
	return 1

def main():
	global localhost

	if len(sys.argv) != 2:
		print("Invalid arguments")
		exit()

	if not sys.argv[1].isdigit():
		print("Invalid arguments")
		exit()

	rsListenPort = int(sys.argv[1])
	print(rsListenPort)

	#create the socket
	try:
		ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("RS Server socket created")
	except socket.error as err:
		print('RS Server socket open error: {}'.format(err))
		exit()

	#bind socket for listening
	binding = ('', rsListenPort)
	ss.bind(binding)

	#listen for connection
	ss.listen(1)
	host = socket.gethostname()
	print("[S]: Server host name is {}".format(host))

	localhost = socket.gethostbyname(host)
	print("[S]: Server IP address is {}".format(localhost))

	#Load data
	buildData()

	#accept connection
	connection, cAddress = ss.accept()
	print ("[S]: Got a connection request from a client at {}".format(cAddress))

	#receive query on loop
	running = 1
	while running == 1:
		data = connection.recv(256) #note, host names are assumed to be <200 chars
		running = handleQuery(data, connection)

	# Close the server socket, never?
	ss.close()
	exit()

main()
