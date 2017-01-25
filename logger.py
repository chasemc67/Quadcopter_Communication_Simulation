# Log stuff to a log file

f = open('log.txt', 'w')

def errorLog(string):
	f.write("[ + ]")
	f.write(string)
	f.write("\n")


def resultsLog(string):
	r = open('results.txt', 'a')
	r.write(string)
	r.write('\n\n')
	r.close()