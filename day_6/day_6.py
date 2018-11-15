

banks = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
numOfBanks = len(banks)

 
def distributeBanks(banks):

	blocksToDistribute = max(banks)
	indexBank = banks.index(blocksToDistribute)

	forAll = blocksToDistribute/numOfBanks
	extra = blocksToDistribute % numOfBanks

	# Remove the blocks from the current bank
	banks[indexBank] = 0

	# Distribute the ones that are equal for all
	banks = list(map(lambda x: x+forAll, banks))

	# Distribute the rest
	while extra > 0:
		indexBank += 1
		if indexBank >= numOfBanks:
			indexBank = 0

		banks[indexBank] += 1
		extra -= 1

	return banks




if __name__ == "__main__":
	stateNumber = 0
	key = ''.join(map(str, banks))
	savedStates = {}

	while key not in savedStates:

		savedStates[key] = stateNumber
		stateNumber += 1

		banks = distributeBanks(banks)
		key = ''.join(map(str, banks))

	print "infinite state: " + str(stateNumber)
	print stateNumber - savedStates[key]
