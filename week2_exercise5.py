'''
	Write a program that asks the user for his/her name and produces an output like:  
		Hi there, what is your name?
		>User input to be read<
		Hello
		“User name”
		How are you?
'''

# I use built-in function input() to ask user for his/her name
# and a variable (name) to store the name inserted by user
name = input("Hi there, what is your name?\n")

# built-in function print() will produce the desired output
print('Hello\n' + name + '\nHow are you?')