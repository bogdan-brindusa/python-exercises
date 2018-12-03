'''
	Expand the above program (5.) by also printing out
	how often the number 7 “fits” into the number
	the user entered.
'''

# variable 'a' holds value inserted by user
a = int(input("Please give an integer number: "))

# using modulo (%) operator to print the remainder
# after division
print("Remainder resulted after dividing %d by\
 7 is: %d" %(a, a%7))

# using floor division (//) to find out how many
# times number 7 'fits' into number 'a'
print("Number of times that 7 'fits' into %d is %d"\
%(a, a//7))