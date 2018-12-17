'''
	Write a class “Student” with a state that stores information
about the students first name, last name, student number and course.
The behaviour of the “Student” class should enable a student object
to get and set each of the Student class variables and to print out
all of the Student’s information.
'''

class Student():
	# constructor (sets each of the Student class variables)
	def __init__(self, firstName = "", lastName = "", studentID = 0, course = ""):
		self.firstName = firstName
		self.lastName = lastName
		self.studentID = studentID
		self.course = course
	
	# method that prints state of object
	def printDetails(self):
		print("First name:\t", self.firstName)
		print("Last name:\t", self.lastName)
		print("Student ID:\t", self.studentID)
		print("Course:\t", self.course)
	
