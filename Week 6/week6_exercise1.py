'''
	 What is the error in this statement? 
		if scoreA = scoreB :   
			print("Tie")
'''

scoreA = 1
scoreB = 2

# the condition from IF statement will give a syntax error because
# we use assignment operator (=) instead of comparison operator (==)
if scoreA = scoreB:
	print("Tie")
