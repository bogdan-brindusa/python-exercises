'''
	Write a program that will ask the user to enter two short sentences and then:  
 
	- Concatenate the two sentences into one long sentence
	- Split the sentence into a list of words
	- Sort the words in alphabetical order and print them out
	- Print the total number of words contained in your list
	- Create a dictionary that will store each word together with the count
	of the occurrence of each word in your sentence.
	- Print each item from the dictionary
'''

# prompt user to insert two sentences
print("Please enter two short sentences.")
sentence1 = input("First sentence: ")
sentence2 = input("Second sentence: ")

sentence3 = sentence1 + ' ' + sentence2	# concatenating sentences

wordsList = sentence3.split()	# split sentence into list of words

wordsList.sort()	# sort the words in alphabetical order
print("Sorted words from these sentences are:\n", wordsList)

print("Total number of words is: %d" %(len(wordsList)))	# print total number of words

wordsDictionary = {}	# dictionary that holds each word together
for word in wordsList:	# with its occurrence
	wordsDictionary[word] = wordsList.count(word)

print("The dictionary that contains each word with its occurrence is:")
for element in wordsDictionary:	# prints elements of dictionary
	print(element, ':\t', wordsDictionary[element])


	
	
	
	
	
	
	
	
	
	
	
	
	
