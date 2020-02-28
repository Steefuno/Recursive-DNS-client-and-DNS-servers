import time
import socket
import sys
import re

addresses = {}
fileName = "PROJI-DNSTS.txt"
ipNotFoundResponse = " - NS"

def buildData():
	global addresses
	global ipNotFoundResponse

	fileObject = open(fileName, "r")
	#makes a list of each line in file
	data = fileObject.readlines()

	for line in data:
		#splits the line into hostname, ip, flag
		lineData = line.split(" ")

		hostName = lineData[0].lower()
		ip = lineData[1]
		flag = re.search(r"\w+", lineData[2]).group()

		#store in dictionary
		addresses[hostName] = ip

def handleQuery(inputString, connection):
	#check if in dictionary of dns
	#if in dictionary, send ip and A
	#else, send TS IP and NS
	response = addresses.get(inputString.lower(), ipNotFoundResponse)

	#format to response message if ip found
	#if not found, it will be formatted as the preset message
	if response != ipNotFoundResponse:
		response = inputString.lower() + " " + response + " A"
	else:
		response = inputString.lower() + ipNotFoundResponse

	connection.send(response.encode('utf-8'))
	return

def main():
	if len(sys.argv) != 2:
		print("Invalid arguments")
		exit()

	if not sys.argv[1].isdigit():
		print("Invalid arguments")
		exit()

	rsListenPort = int(sys.argv[1])

	#create the socket
	try:
		ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error as err:
		print('TS socket open error: {}'.format(err))
		exit()

	#bind socket for listening
	binding = ('', rsListenPort)
	ss.bind(binding)

	#listen for connection
	ss.listen(1)
	host = socket.gethostname()
	print("TS host name: {}".format(host))
	print("TS port: {}".format(rsListenPort))

	localhost = socket.gethostbyname(host)

	#Load data
	buildData()

	#receive query on loop
	while True:
		#accept connection
		connection, cAddress = ss.accept()

		data = connection.recv(256) #note, host names are assumed to be <200 chars
		handleQuery(data, connection)

	# Close the server socket, never?
	ss.close()
	exit()

main()
