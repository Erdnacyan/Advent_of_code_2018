#second part of day 4

import datetime

with open('input.txt', 'r') as fileopen:
	listofdata = fileopen.readlines()

class customObject() :
	def __init__(self, dateti, action):
		self.action = action
		self.dateti = datetime.datetime.strptime(dateti, "%Y-%m-%d %H:%M")

	def __repr__(self):
		return ('Date is:{} and he is :{}'.format(self.dateti, self.action))

listofobj = []
for entry in listofdata:
	newobj = customObject(entry[1:17], entry[19:])
	listofobj.append(newobj)

listofobj.sort(key=lambda x: datetime.date.strftime( x.dateti, "%Y-%m-%d-%H-%M"))


newGroupedObj = []
for entry in listofobj:
	wordlist = entry.action.split(" ")
	if wordlist[0] == "Guard":
		newGroupedObj.append([entry])
	elif wordlist[0] == "falls" or wordlist[0] == "wakes":
		newGroupedObj[-1].append(entry)

# print(newGroupedObj)

# listFromZerotoSixty = []
# for x in range(60):
# 	listFromZerotoSixty.append(0)
# print(listFromZerotoSixty)

guardsDict = {}
for listedentry in newGroupedObj:
	guardID = int(listedentry[0].action.split(" ")[1][1:])
	if guardID not in guardsDict:
		guardsDict[guardID] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

	for x in range(len(listedentry)):
		wordlist = listedentry[x].action.split(" ")
		if wordlist[0] == "falls":
			fallasleepAT = listedentry[x].dateti.minute
			wakeupAT = listedentry[x+1].dateti.minute
			for xthMinute in range(fallasleepAT, wakeupAT):
				guardsDict[guardID][xthMinute] += 1
		elif wordlist[0] == "wakes":
			pass

def findNthMinute(sampleList):
	maxvalue = max(sampleList)
	for x in range(len(sampleList)):
		if sampleList[x] == maxvalue:
			return(maxvalue, x)

maxFrequency = 0
for key,value in guardsDict.items():
	frequency,NthMinute = findNthMinute(value)
	if frequency > maxFrequency:
		maxFrequency = frequency

print(maxFrequency)

#get maxFrequency = 18

def printdict(guardsDict):
	for key,value in guardsDict.items():
		frequency,NthMinute = findNthMinute(value)
		print(value, "\n")

for key,value in guardsDict.items():
	frequency,NthMinute = findNthMinute(value)
	if frequency == 18:
		print(key, NthMinute)

#id = 2999 at 24th minute

print(2999 * 24)

#71976