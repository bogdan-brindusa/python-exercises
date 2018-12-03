'''
	What do the following nested loops display?  Hand trace.  
		
		for i in range(3) : 
			for j in range(1, 4) : 
				print(i + j, end="") 
		print()
'''

for i in range(3): # 'i' takes value of 0, 1, 2
	for j in range(1, 4): # 'j' takes value of 1, 2, 3 
		print(i + j, end = "") 
print() # goes to next line
