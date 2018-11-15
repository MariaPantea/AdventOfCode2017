

''' 
Problem 1 
'''

# Read input
with open('input_1.txt', 'r') as f:
	digits = f.read()

# Convert from string to ints
digits = list(map(lambda x : int(x), digits))


sum_ = 0

for i,digit in enumerate(digits): 

	if i+1 == len(digits):
		next_digit = digits[0]
	else:
		next_digit = digits[i+1]

	if digit == next_digit:
		sum_ += digit


print 'Sum of first problme: ' + str(sum_)




''' 
Problem 2 
'''

# Read input
with open('input_2.txt', 'r') as f:
	digits = f.read()


# Convert from string to ints
digits = list(map(lambda x : int(x), digits))

sum_ = 0
half_way = len(digits)/2

for i,digit in enumerate(digits): 

	next_digit = digits[(i+half_way)%len(digits)]

	if digit == next_digit:
		sum_ += digit


print 'Sum of first problme: ' + str(sum_)

