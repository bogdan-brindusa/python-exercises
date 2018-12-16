'''
	Implement a method 'getPounds' of the 'CashRegister class'
that yields the amount of the total sale as a sterling value
without the pence.
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
		
	# this method returns the integer value of _totalPrice
	def getPounds(self):
		return int(self._totalPrice)

a = CashRegister()
a.addItem(23.25)
print(a.getPounds())