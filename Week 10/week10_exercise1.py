'''
	Consider the class:
	
		class Person():
			def __init__(self, firstName):
				self._name = firstName 
 
	If an object is constructed as harry = Person("Harry")
what is the value of its instance variable _name?
'''

class Person():	# class definition
	def __init__(self, firstName):	# special method to 
									# construct an object
		self._name = firstName	# set up variable _name
			# by assigning it passed argument firstName

harry = Person("Harry")	# creates an object of class Person

print(harry._name)		# prints state of object
