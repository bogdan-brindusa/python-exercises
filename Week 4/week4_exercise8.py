'''
	 Write statements to prompt user for their name and age
	 Write a print statement to output:
		Hello ____, next year you will be ____ years old!
'''

# variable 'name' will store name entered by user
name = input("Insert your name: ")

# variable 'age' will store age entered by user
age = int(input("Insert your age: "))

# print the desired message
print("Hello %s, next year you will be %d years old!" %(name, age + 1))