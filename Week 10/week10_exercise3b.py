'''
		What are the values of register1._itemCount,
	register1._totalPrice, register2._itemCount, and
	register2._totalPrice after these statements? 
 		
		register1 = CashRegister() 
		register1.addItem(0.90) 
		register1.addItem(0.95) 
		register2 = CashRegister() 
		register2.addItem(1.90) 
'''

class CashRegister:
	def __init__(self):
		self._itemCount = 0
		self._totalPrice = 0.0	
	def addItem(self, price):
		self._itemCount = self._itemCount + 1
		self._totalPrice = self._totalPrice + price
	def getTotal(self):
		return self._totalPrice
	def getCount(self):
		return self._itemCount 
	def clear(self):
		self._itemCount = 0
		self._totalPrice = 0.0

register1 = CashRegister()	# creates first object
register1.addItem(0.90)		# call method 'addItem()'
register1.addItem(0.95) 	# call method 'addItem()'
register2 = CashRegister()	# creates second object 
register2.addItem(1.90)		# call method 'addItem()'

print("register1._itemCount = %d" %register1._itemCount)
print("register1._totalPrice = %.2f" %register1._totalPrice)
print("register2._itemCount = %d" %register2._itemCount)
print("register2._totalPrice = %.2f" %register2._totalPrice)