'''
	Consider this recursive function:
	
	def mystery(n):
		if n <= 0:
			return 0
		else:
			return n + mystery(n - 1)
	
	What is mystery(4)?
'''

def mystery(n):	# recursive function
	if n <= 0:
		return 0
	else:
		return n + mystery(n - 1)

print(mystery(4))	# function calling
