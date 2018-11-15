

''' 
Problem 1 
'''
# Read input
with open('input_1.txt', 'r') as f:
	spreadsheet = f.read()


rows = spreadsheet.splitlines()
rows = list(map(lambda x : x.split(), rows))

checksum = 0

for row in rows:
	row = list(map(lambda x : int(x), row))
	checksum += (max(row) - min(row))

print 'Checksum for first problem: ' + str(checksum)



''' 
Problem 2 
'''

# Read input
with open('input_1.txt', 'r') as f:
	spreadsheet = f.read()


rows = spreadsheet.splitlines()
rows = list(map(lambda x : x.split(), rows))

checksum = 0

for row in rows:
	row = (list(map(lambda x : int(x), row)))
	row.sort(reverse=True)

	for n in row:
		isFound = False
		for i in row[1:]:
			if n % i == 0 and n != i:
				checksum += n/i
				isFound = True
				
		if isFound:
			break

print 'Checksum for second problem: ' + str(checksum)



