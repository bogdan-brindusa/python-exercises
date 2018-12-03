'''
	Find the errors in the following if statements, correct where necessary. 
 
	a) if x > 0 then:
			print(x) 
 
	b) if 1 + x > x ** sqrt(2):
			y = y + x
 
	c) if x = 1:
			y += 1
 
	d) letterGrade = "F"
	if grade >= 90:
		letterGrade = "A"
	if grade >= 80:
		letterGrade = "B"
	if grade >= 70:
		letterGrade = "C"
	if grade >= 60:
		letterGrade = "D"
'''

from math import sqrt

x = 3
# 'then' is not a keyword, so it will occur a syntax error
if x > 0 then:
	print(x)

y = 0
if 1 + x > x ** sqrt(2):
	y = y + x

# it must be '==' operator instead of '='
if x = 1:
	y += 1

grade = 50
letterGrade = "F"
if grade >= 90:
	letterGrade = "A"
if grade >= 80:
	letterGrade = "B"
if grade >= 70:
	letterGrade = "C"
if grade >= 60:
	letterGrade = "D"

	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	