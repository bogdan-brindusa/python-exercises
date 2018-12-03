'''
		Write a program that sets a password as “changeme”
	and asks the user to enter the password and keeps asking
	until the correct password is entered and then says
	“Accepted”.  
		The program should count how many attempts the user
	has taken and tell them after they have been accepted.  
		
		Extra Challenge:  
		If the user takes more than 5 attempts the program
	should say, “Access denied, please press enter to exit
	and contact security to reset your password”
'''

# assigning values to chosen variables:
password = 'changeme'
tryPassword = input("Please enter the password: ")
count = 1

# repetitive structure:
while tryPassword != password and count <= 5:
	tryPassword = input("Please try again: ")
	count += 1

# printing message to user
if count < 6:
	print("Password accepted. You've taken %d attempts" %count)
else:
	input("Access denied, please press enter to exit\
 and contact security to reset your password\n")

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 