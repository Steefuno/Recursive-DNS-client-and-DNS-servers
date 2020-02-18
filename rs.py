import time
import socket
import sys

def handleQuery(inputString, connection):
	#check if connection closed
	if inputString == "":
		print("Client Closed: Closing RS\n")
		return 0

	#check if in dictionary of dns
	#if in dictionary, send ip and A
	#else, send TS IP and NS
	print("Received " + inputString)

	response = "You're welcome."
	connection.send(response.encode('utf-8'))
	return 1

def main():
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
		print('RS Server socket open error: {}\n'.format(err))
		exit()

	#bind socket for listening
	binding = ('', rsListenPort)
	ss.bind(binding)

	#listen for connection
	ss.listen(1)
	host = socket.gethostname()
	print("[S]: Server host name is {}".format(host))

	localhost_ip = (socket.gethostbyname(host))
	print("[S]: Server IP address is {}".format(localhost_ip))

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

if __name__ == "__main__":
	main()
