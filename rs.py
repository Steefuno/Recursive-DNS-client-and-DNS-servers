import time
import socket
import sys

def handleQuery(inputString, connection):
	#check if in dictionary of dns
	#if in dictionary, send ip and A
	#else, send TS IP and NS
	print("Received " + inputString)

	response = "You're welcome."
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
	while True:
		#setup try and except around .recv to see when client closes to make it clean
		data = connection.recv(256) #note, host names are assumed to be <200 chars
		handleQuery(data, connection)
		#note, currently errors because client only sends once, then closes

	# Close the server socket, never?
	ss.close()

if __name__ == "__main__":
	main()
