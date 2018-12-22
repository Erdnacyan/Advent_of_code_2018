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

zerothitem = []
for pairs in keylist:
	if pairs[1] == 0 and pairs[0] not in zerothitem:
		zerothitem.append(pairs[0])
zerothitem.sort()

class Worker:
	def __init__(self):
		self.state = "."
		self.time = 0

	def __repr__(self):
		return "this worker is doing " + self.state + " now and done at second: " + str(self.time)

	def findjobs(self, timenow):
		if self.time == timenow:
			for x in instructionDict.keys():
				if self.state in instructionDict[x]:
					instructionDict[x].remove(self.state)
		if zerothitem:
			letter = zerothitem.pop(0)
			timetaken = 60 + ord(letter) - 64
			timefinished = timenow + timetaken
			if len(instructionDict[letter]) == 0:
				del instructionDict[letter]
			print(letter + " starts at " + str(timenow) + " and done at " + str(timefinished))
			self.state = letter
			self.time = timefinished
		else:
			self.state = "."
			self.time = 0

workerDict = {}
for x in range(1,6):
	workerDict[x] = Worker()

timer = 0
while True:
	# for key,value in workerDict.items():
	# 	print(value)
	# for key in instructionDict.keys():
	# 	print(instructionDict[key])
	# print(timer)
	# print(zerothitem)
	# print("\n")
	for x in range(1,6):
		if workerDict[x].state == "." or workerDict[x].time == timer:
			workerDict[x].findjobs(timer)
		keylist = []
		for key,value in instructionDict.items():
			keylist.append([key,len(value)])
		for pairs in keylist:
			if pairs[1] == 0 and pairs[0] not in zerothitem:
				zerothitem.append(pairs[0])
		zerothitem.sort()

	for x in range(1,6):
		if workerDict[x].state == "." or workerDict[x].time == timer:
			workerDict[x].findjobs(timer)
		keylist = []
		for key,value in instructionDict.items():
			keylist.append([key,len(value)])
		for pairs in keylist:
			if pairs[1] == 0 and pairs[0] not in zerothitem:
				zerothitem.append(pairs[0])
	zerothitem.sort()

	if workerDict[1].state == "." and workerDict[2].state == "." and workerDict[3].state == "." and workerDict[4].state == "." and workerDict[5].state == ".":
		break
	timer += 1

print(timer)


