'''
		Using the flow chart provided, construct the if, elif,
	else control structure necessary to implement the flow chart.
		Complete your program to describe the earthquake by asking
	the user to enter a magnitude on the Richter scale and
	print out the effect that magnitude would have had 
	(e.g. “Many buildings destroyed”).
'''

# prompt user to enter a value for magnitude of earthquake
richter = float(input("Enter the magnitude on the Richter scale: "))

# multiple IF statements:
if richter >= 8.0:
	print("Most structures fall")
elif richter >= 7.0:
	print("Many buildings destroyed")
elif richter >= 6.0:
	print("Many buildings considerably damaged, some collapsed")
elif richter >= 4.5:
	print("Damage to poorly constructed buildings")
else:
	print("No destruction of buildings")