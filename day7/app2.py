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
	print("key: %s need :" % (key), value, "\n")
	keylist.append([key,len(value)])

# for list in keylist:
# 	print(list)

workerList = [[".", 0],[".", 0],[".", 0],[".", 0],[".", 0]]
#in each workerList [key, timer]

zerothItem = []
timer = 0
engaged = True
while engaged:
	for eachlist in keylist:
		if eachlist[1] == 0 and eachlist[0] not in zerothItem:
			zerothItem.append(eachlist[0])
	zerothItem.sort()

	for eachWorker in workerList:
		if eachWorker[1] == -1:
			continue
		elif eachWorker[1] == 0:
			if len(zerothItem) != 0:
				keyIn = zerothItem.pop(0)
				keyOut = eachWorker[0]
				eachWorker[0] = keyIn
				eachWorker[1] = 60+ord(keyIn)-64

				print(key, end="")

				if len(instructionDict[keyIn]) == 0:
					del instructionDict[keyIn]

				for x in instructionDict.keys():
					if keyOut in instructionDict[x]:
						instructionDict[x].remove(keyOut)

				keylist = []
				for key,value in instructionDict.items():
					keylist.append([key,len(value)])

				for eachlist in keylist:
					if eachlist[1] == 0 and eachlist[0] not in zerothItem:
						zerothItem.append(eachlist[0])
				zerothItem.sort()
		else:
			eachWorker[1] -= 1
	print(workerList)
	timer += 1

	if workerList == [[],[],[],[],[]]:
		engaged = False

print(timer)

#431