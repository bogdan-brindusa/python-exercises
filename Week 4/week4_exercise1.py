'''
	Explain the mistake in the following code:
		radius = input("Radius:")
		x = 3.14
		pi = x
		area = pi * radius ** 2
'''

radius = input("Radius:")	
# now 'radius' contains a value of type 'string'

x = 3.14
pi = x

# this expression will generate a run-time error,
# because pow() operator must have numeric operands
area = pi * radius ** 2
