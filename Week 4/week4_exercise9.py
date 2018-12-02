'''
	Given that radius is 2 and area is calculated as 12.5678,
	use string format operators to print the values of the
	variables radius and area so that the output looks like this:
		Radius is:         2
		Area is:       12.57
'''

radius = 2
# use format specifiers for desired output
print("%-10s" %("Radius is:"), "%10d" %radius)

area = 12.5678
# use format specifiers for desired output
print("%-10s" %("Area is: "), "%10.2f" %area)