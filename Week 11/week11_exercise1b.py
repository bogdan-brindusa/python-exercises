'''
	Write a program with a main function that imports
the Student class, creates a student object and prints
and changes some of the information (like first name,
last name) of the student object.
'''

# import the module that contains class definition
import week11_exercise1a as mx

def main():	# function definition
	# creating an object of Student class
	student1 = mx.Student("John", "Deere", 123, "Agriculture")
	student1.printDetails()
	
	# modifying object attributes
	student1.firstName = "Mary"
	student1.lastName = "Brown"
	student1.studentID = 321
	student1.course = "Painting"
	
	print("\nNew details of student:\n")
	student1.printDetails()

main()	# function calling
