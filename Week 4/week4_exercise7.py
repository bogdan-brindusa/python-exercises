'''
	Find two run-time errors:
		from math import sqrt
		X = 2
		Y = 4
		print(“The product of “, x, “and”, y, “is”, x + y)
		print(“The root of their difference is “, sqrt(x – y))
'''

from math import sqrt
x = 2
y = 4

# next line will print the sum of x and y, and not the product
# as intended
print("The product of ", x, "and", y, "is", x + y)

#sqrt() will take a negative value, which cause an error
print("The root of their difference is ", sqrt(x - y))
