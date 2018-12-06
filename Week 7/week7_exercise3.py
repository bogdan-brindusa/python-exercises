'''
	What is the output after executing next code block?
'''

nums = []	# creates an empty list
for x in [1,2,3]:
	for y in [3,1,4]:
		if x != y:	# checks this condition for 9 pairs
					# of numbers
			nums.append((x, y))	# add a pair to the list

print(nums)	# prints the list