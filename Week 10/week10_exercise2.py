'''
	Provide an implementation for a Person constructor
	so that after the call p = Person() the _name
	instance variable of p is "unknown".
'''

class Person():				# class definition
	def __init__(self):		# constructor
		self._name = "unknown"	# data field

p = Person()	# creates object of class Person
print(p._name)	# prints state of object
