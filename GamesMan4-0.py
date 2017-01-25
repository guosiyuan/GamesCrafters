initialPosition = [100]

def initial_position() :
	return initialPosition[0]

def primitive(pos) :
	return pos == 0

def gen_moves(pos) :
	if pos>=2:
		return 2 #2 means we can take 2 or can take 1
	elif pos == 1:
		return 1
	else:
		return -1 #no valid next positions

def do_moves(pos, move) :
	if primitive(pos) :
		return -1 #reach the end of game
	elif (pos < move):
		return -1 #can't subtract the move, e.g. pos == 1, move == 2
	elif(move == -1):
		return -1
	else:
		return pos - move

########################################### solver below #################################################

winNumbers = []
loseNumbers = []
def isWin(num):
	if (num in winNumbers):
		return True
	if (num in loseNumbers):
		return False
	if primitive(num):
		loseNumbers.append(num)
		return False
	if (num-1 in loseNumbers) or (num-2 in loseNumbers):
		winNumbers.append(num)
		return True
	if (num-1 in winNumbers) and (num-2 in winNumbers):
		loseNumbers.append(num)
		return False


############################################ solver above, main function below ###################################################

#put the desired number you want to solve down to replace the "20"
for i in range(20):
	print i, isWin(i)  

		
	