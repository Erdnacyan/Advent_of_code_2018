import re

with open('input.txt', 'r') as fileopen:
	datalist = fileopen.readlines()

listofEdges = []
pattern = "Step ([A-Z]) must be finished before step ([A-Z]) can begin"
for eachDatalist in datalist:
	match = re.search(pattern, eachDatalist)
	listofEdges.append([match.group(1), match.group(2)])

instructionDict = {}
for eachEdge in listofEdges:
	if eachEdge[1] not in instructionDict:
		instructionDict[eachEdge[1]] = [eachEdge[0]]
	else:
		instructionDict[eachEdge[1]].append(eachEdge[0])

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for letter in list(letters):
	if letter not in instructionDict:
		instructionDict[letter] = []

keylist = []
for key,value in instructionDict.items():
	# print("key: %s need :" % (key), value, "\n")
	keylist.append([key,len(value)])

# for list in keylist:
# 	print(list)

zerothItem = []
while True:
	for eachlist in keylist:
		if eachlist[1] == 0 and eachlist[0] not in zerothItem:
			zerothItem.append(eachlist[0])
	zerothItem.sort()
	if len(zerothItem) != 0:
		key = zerothItem.pop(0)
	else:
		print("\n")
		break

	print(key, end="")

	if len(instructionDict[key]) == 0:
		del instructionDict[key]

	for x in instructionDict.keys():
		if key in instructionDict[x]:
			instructionDict[x].remove(key)

	keylist = []
	for key,value in instructionDict.items():
		keylist.append([key,len(value)])

#BFKEGNOVATIHXYZRMCJDLSUPWQ