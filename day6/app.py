class coordinatePoints():
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __repr__(self):
		return ("(%i,%i)" % (self.x, self.y))

	def findDistance(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)

# cood ==> [x,y]
def findDistancefromCoord(coordObj, coord):
	return abs(coordObj.x - coord[0]) + abs(coordObj.y - coord[1])

with open('input.txt', 'r') as fileopen:
	datalist = fileopen.readlines()

coordDict = {}
for i in range(len(datalist)):
	x = int(datalist[i].strip().split(",")[0])
	y = int(datalist[i].strip().split(",")[1])
	coordDict[i] = coordinatePoints(x, y)

grid = []
for x in range(500):
	grid.append([])
	for y in range(500):
		grid[x].append("x")

for x in range(500):
	for y in range(500):
		lowestValue = 1000000000000000000000000000000000000000000
		lowestKey = ""
		for key,value in coordDict.items():
			if findDistancefromCoord(value, [x,y]) < lowestValue:
				lowestValue = findDistancefromCoord(value, [x,y])
				lowestKey = key
			elif findDistancefromCoord(value, [x,y]) == lowestValue:
				lowestKey = "."
		grid[x][y] = lowestKey

#check to remove coords that are infinite
infinite = ["x"]
for x in range(500):
	if grid[x][0] not in infinite:
		infinite.append(grid[x][0])

for x in range(500):
	if grid[x][499] not in infinite:
		infinite.append(grid[x][499])

for y in range(500):
	if grid[0][y] not in infinite:
		infinite.append(grid[0][y])

for y in range(500):
	if grid[499][y] not in infinite:
		infinite.append(grid[499][y])



#22, 0 , 20, 12, 41, 49, 28, 32, 23, 10, .


counterDict = {}
for x in range(500):
	for y in range(500):
		if grid[x][y] not in infinite:
			if grid[x][y] not in counterDict:
				counterDict[grid[x][y]] = 1
			else :
				counterDict[grid[x][y]] += 1

maxvalue = 0
for key,value in counterDict.items():
	print(key, value)
	if value > maxvalue:
		maxvalue = value

print(maxvalue)