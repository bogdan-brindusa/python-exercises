'''
	Consider this function that prints a page number
on the left or right side of a page:
		if page % 2 == 0:
			print(page)
		else:
			print("%60s%d" % (" ", page))
	Introduce a function that returns a Boolean
to make the condition in the if statement easier
to understand.
'''

def PrintPageNumber(page):	# function definition
	if EvenPage(page) == True:	# function calling
		print(page)
	else:
		print("%60s%d" % (" ", page))

def EvenPage(nr):	# function definition
	if nr % 2 == 0:
		return True
	else:
		return False

for i in range(2, 10):
	PrintPageNumber(i)	# function calling
	

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
