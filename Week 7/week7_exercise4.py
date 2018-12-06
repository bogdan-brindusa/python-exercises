'''
		Create a program that will keep track of items
	for a shopping list. The program should start
	with an empty list and keep asking for new items
	until nothing is entered (no input followed by
	enter/return key).
		The program should then display the full
	shopping list.
'''

shoppingList = []
status = True

while status == True:
	item = input("Add an item to your shopping list. \
If finish, press Enter/Return key.\n")
	if item == '':
		status = False
	else:
		shoppingList.append(item)

print("Your shopping list is:", shoppingList)
