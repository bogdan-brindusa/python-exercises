'''
	Consider this recursive function:
	
	def mystery(n):
		if n <= 0:
			return 0
		else:
			return mystery(n // 2) + 1
	
	What is mystery(20)?
'''	

def mystery(n):	# recursive function
	if n <= 0:
		return 0
	else:
		return mystery(n // 2) + 1

print(mystery(20))	# function calling