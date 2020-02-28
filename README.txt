Steven Nguyen - shn27
Rithvik Aleshetty - rra76

Implementation of recursive client functionality:
	1. having the client connect to the RS to request an IP
	2. it would get either the IP or, if the RS doesn't have the IP, the IP of the TS
	3. if it gets the TS, the client would request the IP from the TS and either get the IP or say that the IP doesn't exist

Current known issues:
	if the client disconnects at any point except before sending a request or after receiving a response from either TS or RS

Problems:
	Understanding the instructions of the project:
		how many clients can be connected at a time,
		how the TS is shown in DNSRS.txt,
		if and when the server processes should close

Learned Information:
	How to use Python
	