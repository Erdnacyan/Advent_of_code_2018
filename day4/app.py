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

guardsDict = {}

for listedentry in newGroupedObj:
	guardID = int(listedentry[0].action.split(" ")[1][1:])
	if guardID not in guardsDict:
		guardsDict[guardID] = 0	

	for x in range(len(listedentry)):
		wordlist = listedentry[x].action.split(" ")
		if wordlist[0] == "falls":
			time = listedentry[x+1].dateti.minute - listedentry[x].dateti.minute
			guardsDict[guardID] += time
		elif wordlist[0] == "wakes":
			pass

print(guardsDict)

_maxValue = 0
for key in guardsDict:
	if guardsDict[key] > _maxValue:
		_maxValue = guardsDict[key]

for key in guardsDict:
	if guardsDict[key] == _maxValue:
		print(key)

#MR 2411 sleeps the most

Mr2411 = []

for listedentry in newGroupedObj:
	guardID = int(listedentry[0].action.split(" ")[1][1:])
	if guardID == 2411:
		Mr2411.append(listedentry)

print(Mr2411)

timeCounter = {}
for x in range(60):
	timeCounter[x] = 0

def incTime(obj1, obj2):
	lowend = obj1.dateti.minute
	highend = obj2.dateti.minute
	for x in range(lowend, highend):
			timeCounter[x] += 1

for entrylist in Mr2411:
	length = len(entrylist)
	if length == 3:
		incTime(entrylist[1], entrylist[2])
	elif length == 5:
		incTime(entrylist[1], entrylist[2])
		incTime(entrylist[3], entrylist[4])
	elif length == 7:
		incTime(entrylist[1], entrylist[2])
		incTime(entrylist[3], entrylist[4])
		incTime(entrylist[5], entrylist[6])
	elif length == 9:
		incTime(entrylist[1], entrylist[2])
		incTime(entrylist[3], entrylist[4])
		incTime(entrylist[5], entrylist[6])
		incTime(entrylist[7], entrylist[8])

print(timeCounter)

_maxValue2 = 0
for key in timeCounter:
	if timeCounter[key] > _maxValue2:
		_maxValue2 = timeCounter[key]

for key in timeCounter:
	if timeCounter[key] == _maxValue2:
		print(key)

#he sleeps the most at minute 42

print(42 * 2411)

#answer is 101262


####################part 2


