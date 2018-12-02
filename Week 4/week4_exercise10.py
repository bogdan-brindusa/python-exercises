'''
	 What are the values of the following expressions,
	 assuming that p is 17 and q is 18?
		
		i. p // 10 + p % 10 
		ii. p % 2  + q % 2 
		iii. (p + q) // 2 
		iv. (p + q) / 2.0
'''

p = 17
q = 18

# '//' - returns integer quotient
# '%' - returns remainder
# '/' - returns quotient
# '+' - returns sum

i = p // 10 + p % 10
print(i)

ii = p % 2 + q % 2
print(ii)

iii = (p + q) // 2
print(iii)

iv = (p + q) / 2.0
print(iv)
