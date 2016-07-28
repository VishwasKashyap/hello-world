#Defines a "repeat" function that takes 2 arguments
def repeat(s,exclaim):
	"""
	Returns string 's' repeated 3 times.
	If exclaim is true, add exclamation mark
	"""
	result = s+s+s
	if exclaim:
		result = result + '!!!'
	return result

def main():
	print repeat('yay',False)
	print repeat('Woohoo', True)
