'''
	Transform the following instructions into a function
called count_spaces. Define a main function that
will ask the user to enter some input and call the
count_spaces function to return the number of spaces.
	# Counts the number of spaces
	spaces = 0
	for char in userInput:
		if char == " ":
			spaces = spaces + 1
'''

def count_spaces(userInput):	# function definition
	spaces = 0
	for char in userInput:
		if char == " ":
			spaces = spaces + 1
	return spaces
			
def main():	# function definition
	information = input("Please enter any information: ")
	print("Number of spaces in your input is: ",\
count_spaces(information))	# function calling

main()	# main function calling
