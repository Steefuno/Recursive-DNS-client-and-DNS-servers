import socket
import sys

def main():
	if len(sys.argv) != 2:
		print("Invalid Arguments\n")
		exit()

	if not sys.argv[1].isdigit():
		print("Invalid Arguments\n")
		exit()

	port = int(sys.argv[1])
	
	#create socket
	try:
		serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Created server socket\n")
	except socket.error as err:
		print("Failed to create server socket: {}\n".format(err))
		exit()

	#bind socket
	binding = ("localhost", port)
	serverSocket.bind(binding)

	#listen for a connection
	serverSocket.listen(1)

	#accept connection
	connection, client = serverSocket.accept()

	#receive data
	data = connection.recv(128)
	print(data)

	#close socket
	serverSocket.close()
	exit()

main()
