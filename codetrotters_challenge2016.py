# ///////////////////////////////
# 	Israel O. Dilan Pantojas    //
# 	israelodilan@gmail.com      //
#//////////////////////////////// 

#Program description:
print "\n\n\nThis program recieves a integer number in digits notation and returns it's equivalent in english.\n\n"   



#Dictionaries:

# Unit numbers
digits = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8:'eigth', 9: 'nine'}

# Products of ten
products =  {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 2: 'twenty', 3: 'thirty', 4: 'fourty', 5: 'fifty', 6: 'sixty', 7: 'seventy', 8: 'egithy', 9: 'ninety'}

# Powers of ten
powers = {100: 'hundred', 1000: 'thousand', 1000000: 'million'}


# Input prompt and validation:
a = input("\tInput a number from 0 to 999,999,999: ")
while a < 0 or a > 999999999:
	a = input("\t\tPlease, try again: ")

# Build list to translate:
b = []
for e in str(a):
	b.append(int(e))

# List for storing converted output
c = []

#Integer to word function:
def convert(x):
	i = 0
	d = len(x)
	while i != len(x):
		# Testing stubs
		# print "Total length:   " + str(len(x))
		# print "Current length: " + str(d)
		# print "Iterator value: " + str()
		# print "Current Item:   " + str(b[i])
		if b[i] == 0 and len(x) > 1:
			pass
		elif len(x) == 1:	
			c.append(digits[b[i]])
		else:
			if d == 2:
				if b[i] > 1:
					c.append(products[b[i]])
				else:
					c.append(products[int(str(b[i])+str(b[i+1]))])
					d -= 1
					i += 1
			elif d == 3: 
				c.append(digits[b[i]])
				c.append(powers[100])
			elif d == 4: 
				c.append(digits[b[i]])
				c.append(powers[1000])
			elif d == 5:
				if b[i] > 1:
					c.append(products[b[i]])
					if b[i+1] == 0:
						c.append(powers[1000])
				else:
					c.append(products[int(str(b[i])+str(b[i+1]))])
					c.append(powers[1000])
					d -= 1
					i += 1
			elif d == 6:
				c.append(digits[b[i]])
				c.append(powers[100])
				if b[i+1] == 0 and b[i+2] == 0:
					c.append(powers[1000])
			elif d == 7:
				c.append(digits[b[i]])
				c.append(powers[1000000])
			elif d == 8:
				if b[i] > 1:
					c.append(products[b[i]])
					if b[i+1] == 0:
						c.append(powers[1000000])
				else:
					c.append(products[int(str(b[i])+str(b[i+1]))])
					c.append(powers[1000000])
					d -= 1
					i += 1	
			elif d == 9:
				c.append(digits[b[i]])
				c.append(powers[100])
				if b[i+1] == 0 and b[i+2] == 0:
					c.append(powers[1000000])
			else:
				c.append(digits[b[i]])
		d -= 1
		i+=1
		# print c

# Call convert and format print output:
def int_to_word(x):
	convert(x)
	s = ""
	for i in c:
		s += str(i) + " "
	print "\n\n\tOutput: " + s + "\n\n"


# Call int_to_word function:
int_to_word(b)
