import socket
import sys

def main():
	if len(sys.argv) != 3:
		print("Invalid Arguments\n")
		exit()

	if not sys.argv[2].isdigit():
		print("Invalid Arguments\n")
		exit()

	host = sys.argv[1]
	port = int(sys.argv[2])
	
	#create socket
	try:
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		print("Created client socket\n")
	except socket.error as err:
		print("Failed to create client socket: {}\n".format(err))
		exit()

	#connect socket to server's bind
	binding = (host, port)
	clientSocket.connect(binding)

	#send data
	msg = "test test"
	clientSocket.send(msg.encode("utf-8"))

	#close socket
	clientSocket.close()
	exit()

main()
