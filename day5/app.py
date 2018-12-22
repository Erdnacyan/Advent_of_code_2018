with open('input.txt', 'r') as fileopen:
	dataone = fileopen.read()

#65 <--> 97 == 32
#50000

def oldfailedfunction(data):
	engaged = True
	while engaged:
		print(len(data))
		for x in range(len(data)):
			if x == 0:
				if ord(data[x]) >= 97 and ord(data[x]) <= 122:			  #(a - z)
					if data[x+1] == chr(ord(data[x]) - 32):
						data.pop(x)
						data.pop(x+1)
						break
				elif ord(data[x]) >= 65 and ord(data[x]) <= 90:             #(A - Z)
					if data[x+1] == chr(ord(data[x]) + 32):
						data.pop(x)
						data.pop(x+1)
						break
			elif x > (len(data)-1):
				if ord(data[x]) >= 97 and ord(data[x]) <= 122:			  #(a - z)
					if data[x-1] == chr(ord(data[x]) - 32):     
						data.pop(x)
						data.pop(x-1)
						break
				elif ord(data[x]) >= 65 and ord(data[x]) <= 90:       	  #(A - Z)
					if data[x-1] == chr(ord(data[x]) + 32):     
						data.pop(x)
						data.pop(x-1)
						break
			else:
				if ord(data[x]) >= 97 and ord(data[x]) <= 122:			  #(a - z)
					if data[x+1] == chr(ord(data[x]) - 32):
						print(data, "\n")
						print("x:", x)
						data.pop(x)
						data.pop(x+1)
						break
					elif data[x-1] == chr(ord(data[x]) - 32):
						data.pop(x)
						data.pop(x-1)
						break
				elif ord(data[x]) >= 65 and ord(data[x]) <= 90:             #(A - Z)
					if data[x+1] == chr(ord(data[x]) + 32):
						data.pop(x)
						data.pop(x+1)
						break
					elif data[x-1] == chr(ord(data[x]) + 32):
						data.pop(x)
						data.pop(x-1)
						break
		else:
			engaged = False
			return(data)

def newfunction(somelist):
	engaged = True
	while engaged:
		# print(somelist)
		for x in range(len(somelist)):
			if x == len(somelist)-1:
				engaged = False
				return(somelist)
			elif somelist[x].swapcase() == somelist[x+1]:
				somelist.pop(x)
				somelist.pop(x)
				break

datalist = []
oldY = 0
for y in range (500,50000,500):
	datalist.append(dataone[oldY:y])
	oldY = y


newlist = []
for eachdatalist in datalist:
	list2 = list(eachdatalist)
	newlist.extend(newfunction(list2))

finallist = newfunction(newlist)
finalfinallist = newfunction(finallist)

print(finalfinallist)
print(len(finalfinallist))
 
#10556
#10564