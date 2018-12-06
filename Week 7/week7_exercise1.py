'''
	We have a list:
		a = [ 66.25, 333, 333, 1, 1234.5 ]
	We are asked to perform some operations
	on this list.
'''

a = [66.25, 333, 333, 1, 1234.5]

a.insert(2, -1)	# insert '-1' at index 2
a.append(333)	# add '333' at the end of list
print(a)		# [66.25, 333, -1, 333, 1, 1234.5, 333]

print(a.index(333))	# first index of 333

a.remove(333)	# remove first occurence of '333'
print(a)		# [66.25, -1, 333, 1, 1234.5, 333]

a.reverse()	# reverses the order of the list
print(a)	# [333, 1234.5, 1, 333, -1, 66.25]

a.sort()	# sorts the list
print(a)	# [-1, 1, 66.25, 333, 333, 1234.5]
