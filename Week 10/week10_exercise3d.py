'''
	Define and implement a method giveChange(self, payment)
for the CashRegister class that gives change for the provided payment.
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
	
	# method that returns the change for provided payment
	def giveChange(self, payment):
		return (payment - self._totalPrice)

register1 = CashRegister()
register1.addItem(0.90)
register1.addItem(1.20)
print(register1.giveChange(5))