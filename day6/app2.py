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
		totalvalue = 0
		for key,value in coordDict.items():
			totalvalue += findDistancefromCoord(value, [x,y])
		if totalvalue < 10000:
			grid[x][y] = "#"

counterDict = {}
for x in range(500):
	for y in range(500):
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