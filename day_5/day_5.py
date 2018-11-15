
isFirstStar = False

# Read input
with open('input_5.txt', 'r') as f:
	textInput = f.read()

inputList = textInput.splitlines()
maze = list(map(lambda x: int(x), inputList))

pointer = 0
counter = 0

if isFirstStar:
	while(pointer >= 0 and pointer < len(maze)):
		value = maze[pointer]
		maze[pointer] += 1

		pointer += value 
		counter += 1

	print(counter)

else:
	while(pointer >= 0 and pointer < len(maze)):
		value = maze[pointer]

		if value >=3:
			maze[pointer] -= 1
		else:
			maze[pointer] += 1

		pointer += value 
		counter += 1

	print(counter)
