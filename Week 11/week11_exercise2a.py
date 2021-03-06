# A simulated cash register that tracks the item count and
# the total amount looks like this:

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
	def giveChange(self, payment):
		return (payment - self._totalPrice)
	def clear(self):
		self._itemCount = 0
		self._totalPrice = 0.0
