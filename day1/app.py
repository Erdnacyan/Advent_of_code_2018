counter = 0

with open('input.txt', 'r') as fileopen:
	for x in fileopen.readlines():
		value = int(x[1:])
		if x[0] == '+':
			counter += value
		elif x[0] == '-':
			counter -= value

print(counter)

#answer 531

##########  part2

counter2 = 0
newdict = {}
newdict[0] = 1

with open('input.txt', 'r') as fileopen:
	listOfStr = fileopen.readlines()

length = len(listOfStr)

k=0
while k < length + 1:
	if k < length:
		value = int(listOfStr[k][1:])
		if listOfStr[k][0] == '+':
			counter2 += value
		elif listOfStr[k][0] == '-':
			counter2 -= value
		if counter2 in newdict:
			print(counter2)
			break
		else:
			newdict[counter2] = 1
		k += 1
	elif k == length:
		k = 0

#answer 76787