def start():
	"Start Game"
	print('Hello. Adventure waits Ahead.\n\nYou sit at the entrance of a dungeon.\n	')
	dec = 0
	entrance = raw_input('Do you dare to enter? (y,n)\n')
	while (dec == 0):
		if(entrance == 'y'):
			dec = 1;
			goToRoom(0)
		elif(entrance == 'n'):
			print('\nGoodbye!')
			dec = 1;
		else:
			entrance = raw_input('\nInvalid Response. Try Again (y,n)')
	return
def goToRoom(room_no):
	"Select Room"
	if(room_no == 0):
		print('You have entered the Dungeon.\nThere are three hallways in front of you...\nThe left is dimly lit (l), \nThe middle has no light at all (m) \nand the right is completely illuminated by torches (r).\n')
		input0 = raw_input('Which do you choose? (l,m,r)\n')
		while (room_no == 0):
			if(input0 == 'l'):
				print('\nLeft Hallway chosen')
				room_no = 1
			elif(input0 == 'm'):
				print('\nMiddle Hallway chosen')
				room_no = 2
			elif(input0 == 'r'):
				print('\nRight Hallway chosen')
				room_no = 3
			else:
				input0 = raw_input('\nInvalid Response. Try Again (l,m,r)')
	return
#Start Game
start()

