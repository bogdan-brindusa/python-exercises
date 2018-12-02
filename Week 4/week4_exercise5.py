'''
	 Consider the following code:
		x = 19.93
		y = 20.00
		z = y - x
		print(z) 
	The output is 0.0700000000028
	Why is that so?
	Improve the code so that the output is to two decimal places.
'''

x = 19.93
y = 20.00
z = y - x

# the following output is caused by internal representation
# of floating-point numbers
print(z)

# using format specifier for decimal number, output
# will print 2 decimals after point
print("%.2f" %z)