with open('input.txt', 'r') as fileopen:
	listofboxes = fileopen.readlines()

exactlyTwo = 0
exactlyThree = 0

for x in range(len(listofboxes)):
	listofboxes[x] = listofboxes[x].strip()

for y in listofboxes:
	copy = y
	flag2 = True
	flag3 = True
	for eachletter in copy:
		if flag2:
			if y.count(eachletter) == 2:
				exactlyTwo += 1
				flag2 = False
		if flag3:
			if y.count(eachletter) == 3:
				exactlyThree += 1
				flag3 = False
		if (flag2 == False and flag3 == False):
			break

checksum = exactlyTwo * exactlyThree

print(checksum)

#answer 5976


################# part 2

with open('input.txt', 'r') as fileopen:
	listofboxes = fileopen.readlines()


for x in range(len(listofboxes)):
	listofboxes[x] = listofboxes[x].strip()

def compare(word, listofwords):
	for x in listofwords:
		diff = 0
		for i in range(len(word)):
			if word[i] != x[i]:
				diff += 1
		if diff == 1:
			return True #correct box
	else:
		return False

for x in listofboxes:
	if compare(x, listofboxes):
		print(x)

#answer xretqmmonskvzupalfiwhcfdb