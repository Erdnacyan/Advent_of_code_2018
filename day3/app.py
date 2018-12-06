fabric = []

for x in range(1000):
	fabric.append([])

for y in fabric:
	for i in range(1000):
		y.append([0])

with open('input.txt', 'r') as fileopen:
	listofinput = fileopen.readlines()

for eachinput in listofinput:
	getsplit = eachinput.split('@')
	id = getsplit[0]  #still a string

	secsplit = getsplit[1].split(',')
	xcoord = int(secsplit[0])

	thirdsplit = secsplit[1].split(':')
	ycoord = int(thirdsplit[0])

	lastsplit = thirdsplit[1].split('x')
	width = int(lastsplit[0])
	height = int(lastsplit[1])

	for i in range(width):
		for j in range(height):
			fabric[xcoord + i][ycoord + j][0] += 1

fabricCounter = 0

for x in range(1000):
	for y in range(1000):
		if (fabric[x][y][0] > 1):
			fabricCounter += 1

print(fabricCounter)


 # fabric[3][2]
 # 		+5 +2
 # fabric[8][4]

 #answer 101565


 ################part 2

fabric2 = []

for x in range(1000):
	fabric2.append([])

for y in fabric2:
	for i in range(1000):
		y.append([])

with open('input.txt', 'r') as fileopen:
	listofinput = fileopen.readlines()

areaID = {}

for eachinput in listofinput:
	getsplit = eachinput.split('@')
	id = int(getsplit[0][1:])  #still a string

	secsplit = getsplit[1].split(',')
	xcoord = int(secsplit[0])

	thirdsplit = secsplit[1].split(':')
	ycoord = int(thirdsplit[0])

	lastsplit = thirdsplit[1].split('x')
	width = int(lastsplit[0])
	height = int(lastsplit[1])

	areaID[id] = width*height

	for i in range(width):
		for j in range(height):
			fabric2[xcoord + i][ycoord + j].append(id)

dictID = {}

for x in range(1000):
	for y in range(1000):
		if (len(fabric2[x][y]) == 1):
			if fabric2[x][y][0] in dictID:
				dictID[fabric2[x][y][0]] += 1
			else:
				dictID[fabric2[x][y][0]] = 1

for key in dictID:
	if key in areaID:
		if dictID[key] == areaID[key]:
			print(key)

# dict1 = {1:2, 2:3, 3:4}
# dict2 = {1:2, 2:4 , 33:44}
# for key in dict2:
# 	if key in dict1:
# 		print('yes')

#answer 656