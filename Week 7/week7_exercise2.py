'''
	Write a short program to create a list of squares
for numbers up to 10. Start with an empty list called
squares and append squares of numbers from 0 up to 10.
	Print the contents of your list.
'''

squares = []	# crating an empty list
for i in range(0,11):
	squares.append(i**2)	# append elements to list

print(squares)	# prints the list