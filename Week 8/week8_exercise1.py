'''
	Consider this function: 
		def mystery(x, y):
			result = (x + y) / (y - x)
			return result
	What is the result of the call mystery(2, 3)?
'''

def mystery(x, y):	# function definition
	result = (x + y) / (y - x)
	return result

print(mystery(2, 3))	# calling function
