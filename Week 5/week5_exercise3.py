'''
	Explain why the following code won’t really add the two “numbers”: 
 
		number1 = input("Enter first number")
		number2 = input("Enter second number")
		result = number1 + number2
		print(“The result is ”+result)
'''

# the following code block will concatenate two strings,
# even if user inserts numbers
# This is because 'input()' returns a string
number1 = input("Enter first number: ")
number2 = input("Enter second number: ")
result = number1 + number2
print("The result is " + result)
