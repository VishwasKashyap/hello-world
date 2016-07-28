import sys

def Hello(name):
	if name == 'alice' or name == 'Nick':
		name = name + '?????'
		print 'Hello', name
	else:
		print 'else'
	name = name + '!!!!'
	
def main():
	Hello(sys.argv[1])
#Research how to check the functions in a module

if __name__ == '__main__':
	main()
