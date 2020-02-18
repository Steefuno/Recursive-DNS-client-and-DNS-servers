def main():
	#open with read permission
	#r(read), w+(read/write and overwrite), a+(append and read)
	fileObject = open("test.txt", "r")
	
	#read file into string
	contents = fileObject.read()
	print(contents)

	#return to beginning of file
	#(position, offsetType) offset type can be 0(from start), 1(from current), 2(from end)
	#(-5, 2) is 5 chars from end
	fileObject.seek(0, 0) 

	#read file into array split by \n
	contentsList = fileObject.readlines()
	for line in contentsList:
		print(line)

main()
