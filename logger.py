f = open('log.txt', 'w')

def errorLog(string):
	f.write("[ + ]")
	f.write(string)
	f.write("\n")