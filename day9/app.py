marble_position = [0]
current_position = 0
current_marble = 0
next_marble = 1

playerScores = {}
current_player = 1
for x in range(1, 460):
	playerScores[x] = 0

while True:
	current_position = marble_position.index(current_marble)
	if current_marble == 0:
		marble_position.append(1)
		current_marble = next_marble
	elif next_marble % 23 == 0:
		index = current_position - 7
		#careful about this part
		if index < 0:
			index + len(marble_position)
		value_popped = marble_position.pop(index)
		playerScores[current_player] += (value_popped + next_marble)
		current_marble = marble_position[index]
	else:
		if len(marble_position) < current_position + 2:
			index = (current_position + 2) % len(marble_position)
		else:
			index = current_position + 2
		marble_position.insert(index, next_marble)
		current_marble = next_marble
	next_marble += 1
	if current_player == 459:
		current_player = 1
	else:
		current_player += 1
	# print(marble_position)
	if next_marble == 72104:
		break

max_score = 0
for key in playerScores:
	if playerScores[key] > max_score:
		max_score = playerScores[key]

print(max_score)

#390211 is too hai