'''
	 Write a program that asks the user for an
	 integer number and then prints out the
	 remainder after the number is divided by 7.
'''

# variable 'a' holds value inserted by user
a = int(input("Please give an integer number: "))

# using modulo (%) operator to print the remainder
# after division
print("Remainder resulted after dividing %d by\
 7 is: %d" %(a, a%7))