'''
	 Write a program that asks for two numbers (Python has all the basic mathematical
	 functions in place, like +, - etc.), adds them up and displays the result.
'''

# I use built-in function input() to ask user for a value
# because input() returns a string, I'll convert the returned value to integer
a = int(input("Give a value for first number: "))
b = int(input("Give a value for second number: "))

# variable sum will hold the result of sum between a and b
sum = a + b

# built-in function print() displays value of variable sum
print("Sum of these numbers is: %d" %sum)
