'''
	Explain the mistake in the following code:
		radius = input(float("Enter the radius:"))
'''

# an error will occur when trying to convert 'string'
# ("Enter the radius: ") to 'float'

# this conversion is not possible
radius = input(float("Enter the radius:"))