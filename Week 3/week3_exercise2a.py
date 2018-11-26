'''
	What will the output be from the following code?
		num = 4
		num *= 2
		num1 = num + 2
		num1 += 3
		print(num1)
'''

num = 4			# assign value 4 to variable 'num'

num *= 2		# same as 'num = num * 2'
				# new value of 'num' will be 8 (4 * 2)
				
num1 = num + 2	# num1 = 8 + 2, so num1 = 10

num1 += 3		# same as 'num1 = num1 + 3'
				# new value of 'num1' will be 13 (10 + 3)
				
print(num1)		# prints '13'
