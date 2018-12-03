'''
	Write a program that will generate a table
	to print powers of the first 5 numbers.
	Your output should be similar to the sample
	given.
'''

# this task requires use of 'for' loops

# print first line of table using format specifier
print(end = '  ')
for i in range(1, 4):
	print("%-6d" %i, end = '')
print()

# print second line of table using format specifier
print(end = ' ')
for i in range(1, 4):
	print("%-6s" %('x'), end = '')
print()

# print third line of table (line)
for i in range(18):
	print('-', end = '')
print()

# print rows of table
for i in range(1, 6):
	print(end = '  ')
	for j in range(1, 4):
		print("%-6d" %(i**j), end = '')
	print()
	
	
	
	
	
	
	
	
	
	
	
	
	
	