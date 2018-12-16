'''
	A simulated cash register that tracks the item count
and the total amount looks like the above code.
	Add comments to explain the code as requested.
'''

class CashRegister:
	# first method is the constructor (invoked to create
	# a new object), that provide the opportunity to set
	# up the instance with variables (data fields)
	def __init__(self):
		self._itemCount = 0
		self._totalPrice = 0.0
	
	# next methods define the bahaviour of an object
	# first method modify data fields of object by adding
	# some values to existing ones ('price' is an argument
	# of method)
	def addItem(self, price):
		self._itemCount = self._itemCount + 1
		self._totalPrice = self._totalPrice + price
	
	# this method returns the value of variable
	# '_totalPrice' (is an attribute of object)
	def getTotal(self):
		return self._totalPrice
	
	# returns value of variable '_itemCount' (attribute of
	# object)
	def getCount(self):
		return self._itemCount 
	
	# this method reset the value of data fields (variables)
	# to zero
	def clear(self):
		self._itemCount = 0
		self._totalPrice = 0.0
