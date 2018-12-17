# Write a TestRegister class to test the addItem, getTotal,
# getCount and giveChange methods of the CashRegister class

# import module that contains CashRegister class definition
import week11_exercise2a as my

# class that inherits CashRegister class found in imported module
class TestRegister(my.CashRegister):
	def __init__(self):
		my.CashRegister.__init__(self)
	# I will not override methods from parent class
	# I don't define any new methods
	
register1 = TestRegister()	# creates an object of TestRegister class

# test the methods of CashRegister class that are inherited by
# TestRegister class
register1.addItem(0.80)
register1.addItem(1.30)
print(register1.getTotal())
print(register1.getCount())
print(register1.giveChange(10))