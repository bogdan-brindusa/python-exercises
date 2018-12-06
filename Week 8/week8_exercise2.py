'''
	What does this program print?
		def main():
			a = 5
			b = 7
			print(mystery(a, b))
		def mystery(x, y):
			z = x + y
			z = z / 2.0
			return z
		main()
'''

def main():	# function definition
	a = 5
	b = 7
	print(mystery(a, b))	# calling function

def mystery(x, y):	# function definition
	z = x + y
	z = z / 2.0
	return z

main()	# calling function