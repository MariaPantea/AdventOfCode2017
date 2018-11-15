

def isValid(passPhrase):
	passWords = passPhrase.split(" ")
	return len(passWords) == len(set(passWords))

def isValid2(passPhrase):
	passWords = passPhrase.split(" ")
	sortedPassWords = list(map(lambda w : ''.join(sorted(w)), passWords))
	return len(sortedPassWords) == len(set(sortedPassWords))




# Read input
with open('input1.txt', 'r') as f:
	input = f.read()

passPhrases = input.splitlines()
print(len(list(filter(isValid, passPhrases))))
print(len(list(filter(isValid2, passPhrases))))
